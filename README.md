# 🚀 API de Consulta de CNPJ e Validação de CPF

API desenvolvida em **FastAPI** para consulta de dados cadastrais de empresas (CNPJ) utilizando bases abertas gratuitas e validação matemática de CPFs (dígitos verificadores), respeitando as diretrizes da LGPD.

---

## 📋 Sumário
1. [Tecnologias Utilizadas](#tecnologias-utilizadas)
2. [Estrutura do Projeto](#estrutura-do-projeto)
3. [Como Instalar e Executar](#como-instalar-e-executar)
4. [Documentação da API (Endpoints)](#documentação-da-api-endpoints)
5. [Como Integrar em Outros Sistemas](#como-integrar-em-outros-sistemas)
   - [Exemplo em Python (Requests)](#exemplo-em-python-requests)
   - [Exemplo em JavaScript / Node.js (Fetch)](#exemplo-em-javascript--nodejs-fetch)
   - [Exemplo em PHP (cURL)](#exemplo-em-php-curl)

---

## 🛠 Tecnologias Utilizadas
* **Python 3.10+**
* **FastAPI** (Framework web de alta performance)
* **Uvicorn** (Servidor ASGI)
* **HTTPX** (Cliente HTTP assíncrono para consumo da BrasilAPI)

---

## ⚙️ Como Instalar e Executar

Clone o repositório e configure o ambiente localmente:

```bash
# 1. Clone o repositório
git clone [https://github.com/SEU_USUARIO/cnpj-consult-api.git](https://github.com/SEU_USUARIO/cnpj-consult-api.git)
cd cnpj-consult-api

# 2. Crie e ative um ambiente virtual (Opcional, mas recomendado)
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

# 3. Instale as dependências
pip install fastapi uvicorn httpx

# 4. Inicie o servidor da API
uvicorn main:app --reload
