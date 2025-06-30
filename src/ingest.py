import os, glob
from langchain.document_loaders import TextLoader, PyPDFLoader, UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
from tqdm import tqdm

CHUNK_SIZE = 1024
CHUNK_OVERLAP = 128

def load_documents(data_dir: str):
    docs = []
    patterns = ('*.txt', '*.md', '*.pdf')
    for pattern in patterns:
        for filepath in glob.glob(os.path.join(data_dir, '**', pattern), recursive=True):
            if filepath.endswith('.txt'):
                docs.extend(TextLoader(filepath, encoding='utf-8').load())
            elif filepath.endswith('.md'):
                docs.extend(UnstructuredMarkdownLoader(filepath).load())
            elif filepath.endswith('.pdf'):
                docs.extend(PyPDFLoader(filepath).load())
    return docs

def main():
    load_dotenv()
    data_dir = os.getenv('DATA_DIR', 'data')
    vector_dir = os.getenv('VECTOR_STORE_DIR', 'vectorstore')

    print(f"📄 A carregar documentos de {data_dir} ...")
    docs = load_documents(data_dir)
    if not docs:
        print('⚠️  Nenhum documento encontrado!')
        return

    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    print('🔪 A dividir documentos em chunks ...')
    chunks = splitter.split_documents(docs)

    print('⚙️  A criar embeddings ...')
    embedder = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    vectordb = FAISS.from_documents(chunks, embedder)

    os.makedirs(vector_dir, exist_ok=True)
    vectordb.save_local(vector_dir)
    print(f'✅ Vector store gravado em {vector_dir}')

if __name__ == '__main__':
    main()
