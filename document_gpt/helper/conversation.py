from config import config
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# prompt_template = """Use the following pieces of context to answer the question at the end. \ 
#     If you don't know the answer, just say that you don't know, don't try to make up an answer. \

#     {context} \

#     Question: {question}"""

# PROMPT = PromptTemplate(
#     template=prompt_template, input_variables=["context", "question"])

# chain_type_kwargs = {"prompt": PROMPT}


def create_conversation() -> RetrievalQA:

    persist_directory = config.DB_DIR

    embeddings = OpenAIEmbeddings(
        openai_api_key=config.OPENAI_API_KEY
    )

    db = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )

    qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(),
        chain_type='stuff',
        retriever=db.as_retriever(),
        # chain_type_kwargs=chain_type_kwargs,
        verbose=True
    )

    return qa
