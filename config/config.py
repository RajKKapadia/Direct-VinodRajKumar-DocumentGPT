import os

from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from openai import OpenAI

load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_MODEL_NAME = 'gpt-3.5-turbo-0125'

TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_TOKEN = os.getenv('TWILIO_TOKEN')
FROM = os.getenv('FROM')

CONNECTION_STRING = os.getenv('CONNECTION_STRING')
DATABASE_NAME = os.getenv('DATABASE_NAME')
COLLECTION_NAME = os.getenv('COLLECTION_NAME')

cwd = os.getcwd()

DB_DIR = os.path.join(
    cwd,
    'data',
    'db'
)
os.makedirs(DB_DIR, exist_ok=True)

OUTPUT_DIR = os.path.join(
    cwd,
    'data',
    'output'
)
os.makedirs(OUTPUT_DIR, exist_ok=True)

embeddings = OpenAIEmbeddings(
    openai_api_key=OPENAI_API_KEY,
    model='text-embedding-3-large'
)

chat_model = ChatOpenAI(
    temperature=0,
    openai_api_key=OPENAI_API_KEY,
    model_name=OPENAI_MODEL_NAME
)

openai_client = OpenAI(
    api_key=OPENAI_API_KEY
)
