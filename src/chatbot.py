import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import LlamaCpp
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate


def main() -> None:
    load_dotenv()

    vector_dir = os.getenv("VECTOR_STORE_DIR", "vectorstore")
    model_path = os.getenv(
        "MODEL_PATH",
        "models/llama/llama-3-8b-instruct.Q4_K_M.gguf",
    )

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Modelo não encontrado: {model_path}")

    # 1. Carregar o vector store
    embedder = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    db = FAISS.load_local(
        vector_dir, embedder, allow_dangerous_deserialization=True
    )
    retriever = db.as_retriever(search_kwargs={"k": 4})

    # 2. Definir o prompt
    template = (
        "Você é um assistente especializado em saúde, focado em cuidados básicos "
        "e prevenção de doenças comuns.\n"
        "Utilize estritamente o contexto abaixo para responder.\n"
        "Se não souber, diga que não sabe!\n\n"
        "{context}\n\n"
        "Pergunta: {question}\n"
        "Resposta:"
    )
    prompt = PromptTemplate(
        template=template, input_variables=["context", "question"]
    )

    # 3. Carregar o LLM
    llm = LlamaCpp(
        model_path=model_path,
        n_ctx=4096,
        temperature=0.2,
        top_p=0.95,
        n_gpu_layers=35,
    )

    # 4. Construir a chain RAG
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=False,
        chain_type_kwargs={"prompt": prompt},
    )

    # 5. Loop de conversa
    print("🤖 Chatbot pronto! Digite 'sair' para terminar.")
    while True:
        question = input("Você: ")
        if question.lower() in {"sair", "exit", "quit"}:
            break
        response = qa_chain({"query": question})
        print(f'Bot: {response["result"]}\n')


if __name__ == "__main__":
    main()
