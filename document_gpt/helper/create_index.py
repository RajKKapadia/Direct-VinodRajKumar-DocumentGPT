from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_community.vectorstores import Chroma
from pypdf import PdfReader

from config import config


def create_index(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text()

    with open(f'{config.OUTPUT_DIR}/output.txt', 'w') as file:
        file.write(text)
        loader = DirectoryLoader(
            config.OUTPUT_DIR,
            glob='**/*.txt',
            loader_cls=TextLoader
        )
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1024,
        chunk_overlap=64
    )
    texts = text_splitter.split_documents(documents)
    persist_directory = config.DB_DIR
    vectordb = Chroma.from_documents(
        documents=texts,
        embedding=config.embeddings,
        persist_directory=persist_directory
    )
    vectordb.persist()
