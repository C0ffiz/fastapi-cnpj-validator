from fastapi import FastAPI, HTTPException, Query
import httpx
import re

app = FastAPI(
    title="API de Consulta CNPJ e Validação CPF",
    description="API gratuita para consulta de CNPJ (via dados abertos) e validação de CPF.",
    version="1.0.0"
)

# Função utilitária para limpar caracteres especiais
def limpar_documento(doc: str) -> str:
    return re.sub(r'\D', '', doc)

# Validação matemática de CPF (Dígitos Verificadores)
def validar_cpf_math(cpf: str) -> bool:
    cpf = limpar_documento(cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    
    # Validação do 1º dígito
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0
    if digito1 != int(cpf[9]):
        return False
        
    # Validação do 2º dígito
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0
    if digito2 != int(cpf[10]):
        return False
        
    return True

@app.get("/")
def home():
    return {"status": "online", "endpoints": ["/cnpj/{cnpj}", "/cpf/validar/{cpf}"]}

@app.get("/cnpj/{cnpj}")
async def consultar_cnpj(
    cnpj: str, 
    detalhado: bool = Query(True, description="Retornar dados completos ou filtrados básicos")
):
    """
    Consulta dados de um CNPJ utilizando bases abertas gratuitas.
    Filtros disponíveis via parâmetro 'detalhado'.
    """
    cnpj_limpo = limpar_documento(cnpj)
    
    if len(cnpj_limpo) != 14:
        raise HTTPException(status_code=400, detail="CNPJ inválido. Deve conter 14 dígitos.")
    
    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj_limpo}"
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=10.0)
            if response.status_code == 404:
                raise HTTPException(status_code=404, detail="CNPJ não encontrado.")
            elif response.status_code != 200:
                raise HTTPException(status_code=response.status_code, detail="Erro ao consultar o serviço de CNPJ.")
            
            data = response.json()
            
            # Se o usuário quiser dados filtrados/resumidos
            if not detalhado:
                return {
                    "cnpj": data.get("cnpj"),
                    "razao_social": data.get("razão_social"),
                    "nome_fantasia": data.get("nome_fantasia"),
                    "situacao": data.get("descricao_situacao_cadastral"),
                    "porte": data.get("porte"),
                    "municipio": data.get("municipio"),
                    "uf": data.get("uf")
                }
            
            return data
            
        except httpx.RequestError:
            raise HTTPException(status_code=500, detail="Falha de conexão com o provedor de dados de CNPJ.")

@app.get("/cpf/validar/{cpf}")
def validar_cpf(cpf: str):
    """
    Valida a estrutura matemática e os dígitos verificadores de um CPF.
    (Por restrições da LGPD, consultas de dados cadastrais de CPFs exigem APIs pagas e homologadas).
    """
    cpf_limpo = limpar_documento(cpf)
    
    if len(cpf_limpo) != 11:
        raise HTTPException(status_code=400, detail="CPF deve conter 11 dígitos.")
    
    valido = validar_cpf_math(cpf_limpo)
    
    return {
        "cpf": cpf_limpo,
        "valido": valido,
        "mensagem": "CPF estruturalmente válido." if valido else "CPF inválido (dígitos verificadores incorretos)."
    }