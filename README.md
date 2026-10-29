# 🚀 API de Consulta de CNPJ e Validação de CPF

API desenvolvida em **Python** utilizando **FastAPI** para consulta gratuita de dados cadastrais de empresas (CNPJ) através de bases abertas e validação matemática de CPFs (dígitos verificadores), em conformidade com as diretrizes da LGPD.

---

## 📋 Sumário
1. [Tecnologias Utilizadas](#-tecnologias-utilizadas)
2. [Guia Passo a Passo para Iniciantes (Windows)](#-guia-passo-a-passo-para-iniciantes-windows)
3. [Como Executar no Linux / macOS](#-como-executar-no-linux--macos)
4. [Documentação da API (Endpoints)](#-documentação-da-api-endpoints)
5. [Como Testar no Navegador](#-como-testar-no-navegador)
6. [Como Integrar em Outros Sistemas](#-como-integrar-em-outros-sistemas)

---

## 🛠 Tecnologias Utilizadas
* **Python 3.10+**
* **FastAPI** (Framework web de alta performance)
* **Uvicorn** (Servidor Web ASGI)
* **HTTPX** (Cliente HTTP assíncrono para consumo da BrasilAPI)

---

## 🔰 Guia Passo a Passo para Iniciantes (Windows)

Se você não tem experiência prévia com programação, siga estas instruções simples para rodar a API no seu computador:

### 1. Instalar o Python no Windows
1. Acesse o site oficial: [python.org/downloads](https://www.python.org/downloads/)
2. Clique no botão de download da versão mais recente.
3. **⚠️ IMPORTANTE:** Ao abrir o instalador, marque a caixa na parte inferior: **"Add python.exe to PATH"** (Adicionar o Python ao PATH).
4. Clique em **Install Now** e aguarde a conclusão.

### 2. Criar a Pasta do Projeto
1. Vá até a sua **Área de Trabalho** (Desktop).
2. Crie uma nova pasta chamada **`api-documentos`**.

### 3. Criar o Arquivo do Código
1. Abra o **Bloco de Notas** do Windows.
2. Copie o código Python da API e cole dentro do Bloco de Notas.
3. Clique em **Arquivo > Salvar Como...**
4. Navegue até a pasta `api-documentos` no Desktop.
5. Em *Nome do arquivo*, digite: `main.py`
6. Em *Tipo*, mude de `Documentos de Texto (*.txt)` para **`Todos os arquivos (*.*)`**.
7. Clique em **Salvar**.

### 4. Instalar as Ferramentas pelo Terminal
1. Abra o Menu Iniciar do Windows, digite **PowerShell** (ou **cmd**) e abra o aplicativo.
2. Acesse a pasta do projeto digitando o comando:
   ```powershell
   cd Desktop\api-documentos
   ```
3. Instale os pacotes necessários rodando o comando:
   ```powershell
   pip install fastapi uvicorn httpx
   ```

### 5. Executar a API
1. Ainda no PowerShell (dentro da pasta `api-documentos`), digite:
   ```powershell
   uvicorn main:app --reload
   ```
2. Quando a mensagem `Uvicorn running on http://127.0.0.1:8000` aparecer, **a sua API já estará no ar!**
3. *Mantenha a janela do PowerShell aberta enquanto estiver utilizando a API.*

---

## 🐧 Como Executar no Linux / macOS

```bash
# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/cnpj-consult-api.git
cd cnpj-consult-api

# 2. Crie e ative um ambiente virtual (Opcional, mas recomendado)
python3 -m venv venv
source venv/bin/activate

# 3. Instale as dependências
pip install fastapi uvicorn httpx

# 4. Inicie o servidor
uvicorn main:app --reload
```

---

## 📍 Documentação da API (Endpoints)

### 1. Consultar CNPJ
Retorna os dados cadastrais completos ou resumidos de uma empresa.
* **URL:** `/cnpj/{cnpj}`
* **Método:** `GET`
* **Parâmetro de Consulta (Query):**
  * `detalhado` *(booleano, opcional)*: `true` (padrão) para dados completos, `false` para dados resumidos.

### 2. Validar CPF
Realiza a validação matemática da estrutura e dos dígitos verificadores de um CPF.
* **URL:** `/cpf/validar/{cpf}`
* **Método:** `GET`

---

## 🌐 Como Testar no Navegador

Com o servidor rodando (`uvicorn`), abra seu navegador de preferência e acesse:

* **Testar Validação de CPF:**
  ```text
  http://127.0.0.1:8000/cpf/validar/11144477735
  ```

* **Testar Consulta de CNPJ Resumida:**
  ```text
  http://127.0.0.1:8000/cnpj/04205747000137?detalhado=false
  ```

* **Interface Visual Interativa (Swagger UI):**
  Acesse a documentação interativa para testar os endpoints direto na tela sem digitar comandos:
  ```text
  http://127.0.0.1:8000/docs
  ```

---

## 🔌 Como Integrar em Outros Sistemas

Você pode consumir esta API em qualquer linguagem de programação ou sistema web/ERP.

### 🐍 Python (`requests`)
```python
import requests

url = "http://127.0.0.1:8000/cnpj/04205747000137?detalhado=false"
response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    print(f"Empresa: {dados.get('razao_social')}")
    print(f"Situação: {dados.get('situacao')}")
```

### 🟨 JavaScript / Node.js (`fetch`)
```javascript
async function consultarCNPJ(cnpj) {
    try {
        const response = await fetch(`http://127.0.0.1:8000/cnpj/${cnpj}?detalhado=false`);
        if (!response.ok) throw new Error("CNPJ não encontrado");
        
        const data = await response.json();
        console.log("Razão Social:", data.razao_social);
        console.log("Situação:", data.situacao);
    } catch (error) {
        console.error("Erro:", error.message);
    }
}

consultarCNPJ("04205747000137");
```

### 🐘 PHP (`cURL`)
```php
<?php
$cnpj = "04205747000137";
$url = "http://127.0.0.1:8000/cnpj/" . $cnpj . "?detalhado=false";

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

if ($httpCode === 200) {
    $data = json_decode($response, true);
    echo "Razão Social: " . $data['razao_social'];
} else {
    echo "Erro na consulta de CNPJ.";
}
?>
```
