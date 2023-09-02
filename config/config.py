import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
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
