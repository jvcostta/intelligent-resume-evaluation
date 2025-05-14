# 🧠 Intelligent Resume Evaluation

Este projeto é uma aplicação de análise inteligente de currículos em PDF. Utiliza **FastAPI** como backend, **PyMuPDF** para extração de texto de arquivos PDF, e integra com o modelo **LLaMA3 via API da Groq** para gerar uma análise profissional e personalizada dos dados extraídos.

---

## 📌 Funcionalidades

- 📄 Upload de currículos em PDF.
- 🧠 Extração automática de informações relevantes do currículo.
- 🤖 Análise de conteúdo por um LLM (modelo de linguagem) hospedado na plataforma **Groq**.
- 🧾 Geração de resposta textual com feedback sobre o currículo.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.10**
- **FastAPI** (framework web)
- **PyMuPDF** (`fitz`) para extração de PDF
- **HTTPX** para requisições assíncronas à API da Groq
- **Uvicorn** como servidor ASGI
- **Groq API** com modelo LLaMA3

---

## ⚙️ Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/intelligent-resume-evaluation.git
cd intelligent-resume-evaluation
```

### 2. Crie um ambiente virtual (boa prática)

```bash
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure a variável de ambiente da API da Groq
Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
```bash
GROQ_API_KEY=sua_chave_aqui
```

### 5. Rode a aplicação
```bash
uvicorn app.main:app --reload
```
### 6. Acesse a documentação automática da API em:
```bash
http://localhost:8000/docs
```