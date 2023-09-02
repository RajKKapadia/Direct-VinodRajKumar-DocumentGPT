from config import config
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory


def create_conversation(query: str, chat_history: list) -> RetrievalQA:
    persist_directory = config.DB_DIR
    embeddings = OpenAIEmbeddings(
        openai_api_key=config.OPENAI_API_KEY
    )
    db = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )
    memory = ConversationBufferMemory(
        memory_key='chat_history',
        return_messages=False
    )
    cqa = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(
            temperature=0.0,
            openai_api_key=config.OPENAI_API_KEY),
        retriever=db.as_retriever(),
        memory=memory,
        get_chat_history=lambda h: h,
        verbose=True
    )
    result = cqa({'question': query, 'chat_history': chat_history})
    return result['answer']
