# 🧠 Mini Chatbot RAG – Saúde

## Visão geral
Este projeto implementa um **chatbot inteligente** baseado em RAG (*Retrieval-Augmented Generation*) que responde perguntas sobre **cuidados básicos de saúde e prevenção de doenças comuns**, como malária, hipertensão, diarreia, entre outros.

---

## 📌 Tema

**Saúde – Cuidados Básicos e Prevenção de Doenças Comuns**

---

## ❓ Por que escolhi este tema?

Num contexto onde muitas comunidades têm **acesso limitado a profissionais de saúde** e onde circulam informações pouco confiáveis, este chatbot pode ajudar a promover a **educação em saúde básica**, fornecendo respostas baseadas em documentos reais e confiáveis. Além disso, o tema é **relevante e útil para todos**, independentemente da idade ou escolaridade.

---

## 🤖 Como o RAG pode ajudar?

A técnica RAG permite que um modelo de linguagem (LLM) **não invente respostas**, mas sim se baseie em **documentos reais** para responder a perguntas. Isso é feito em 3 etapas:

### ⚙️ Técnica RAG resumida

1. **R – Retrieve**  
   O sistema procura nos documentos os trechos mais relevantes para a pergunta feita.

2. **A – Augment**  
   Esses trechos são inseridos no *prompt* enviado ao modelo.

3. **G – Generate**  
   O modelo LLM (Llama) gera uma resposta baseada **somente no conteúdo recuperado**, reduzindo "alucinações".

---

## 🗂️ Estrutura do projeto

mini_chatbot_rag/

├── app.py # Ponto de entrada principal

├── data/ # Pasta com documentos (.pdf, .txt, .md)

├── vectorstore/ # Vector store FAISS (gerado após ingestão)

├── models/llama/ # Modelo GGUF do Llama

├── utils/

│ └── preprocess.py # Script que carrega e divide documentos

├── .env # Variáveis de ambiente

├── requirements.txt

└── README.md

---

## 🚀 Como executar o projeto (Windows 10/11 + VSCode)

### 1. ⚙️ Pré-requisitos

- Python 3.10+
- VSCode com extensão Python
- Git (opcional)
- Compilador C++ se quiser usar Llama com GPU

---

### 2. ⬇️ Clonar ou extrair o projeto

Se for ZIP:

```powershell
cd C:\Users\teu_nome\Desktop
Expand-Archive .\mini_chatbot_rag.zip
cd .\mini_chatbot_rag\

```
### 3. 🧪 Criar ambiente virtual

py -3.10 -m venv .venv
.\.venv\Scripts\activate

```
```

### 4. 📦 Instalar dependências
pip install --upgrade pip
pip install -r requirements.txt
pip install unstructured  # Corrige erro de PDF


### 5. 📝 Editar o .env

Exemplo de conteúdo:
DATA_DIR=data
VECTOR_STORE_DIR=vectorstore
MODEL_PATH=models/llama/Llama-3-8b-instruct.Q4_K_M.gguf

```
```
### 6. 📁 Adicionar documentos sobre saúde
Coloque 10–50 ficheiros .txt, .pdf ou .md dentro da pasta data/.


### 7. 🧠 Criar o vector store (ingestão dos dados)
python app.py

Ele vai:
- Carregar os documentos
- Dividir em trechos (chunks)
- Gerar os vetores (embeddings)
- Criar o vector store

### 8. 💬 Usar o chatbot
Depois de criada a base, o chatbot pode ser ativado via terminal (ou por notebook, se incluído).

🧠 Modelo LLM usado
- Llama-3-8B-Instruct (formato .gguf)
- Quantização recomendada: Q4_K_M
- Coloca o ficheiro .gguf na pasta: models/llama/

Modelos podem ser baixados de:
👉 https://huggingface.co/TheBloke

✅ Exemplo de uso
Você: Como posso prevenir a malária?
Bot: Para prevenir a malária, recomenda-se o uso de redes mosquiteiras, repelentes e evitar águas paradas...

📌 Notas
- Todos os dados são locais: funciona offline.
- Pode-se expandir com novos temas apenas adicionando documentos.
- Ideal para contextos educacionais, rurais ou com baixo acesso à internet.

🪪 Licença
Uso académico e educacional.
Confirma sempre a licença dos documentos e modelos usados.