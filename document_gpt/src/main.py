from datetime import datetime
import time

from flask import Flask, request

from document_gpt.helper.conversation import create_conversation
from document_gpt.helper.twilio_api import send_message
from document_gpt.helper.utils import get_chat_history_from_mongodb, create_string_chunks
from document_gpt.helper.database import create_user, update_messages, get_user

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return 'OK', 200


@app.route('/twilio', methods=['POST'])
def twilio():
    query = request.form['Body']
    sender_id = request.form['From']
    print(sender_id, query)
    user = get_user(sender_id)
    if user:
        chat_history = get_chat_history_from_mongodb(user['messages'][-2:])
        response = create_conversation(query, chat_history)
        update_messages(sender_id, query,
                        response, user['messageCount'])
        sentences = create_string_chunks(response, 1500)
        for s in sentences:
            send_message(sender_id, s)
            time.sleep(1.0)
    else:
        response = create_conversation(query, [])
        message = {
            'query': query,
            'response': response,
            'createdAt': datetime.now().strftime('%d/%m/%Y, %H:%M')
        }
        user = {
            'userName': '',
            'senderId': sender_id,
            'messages': [message],
            'messageCount': 1,
            'mobile': '',
            'email': '',
            'channel': 'WhatsApp',
            'created_at': datetime.now().strftime('%d/%m/%Y, %H:%M'),
            'status': 'inactive'
        }
        create_user(user)
        send_message(sender_id, response)

    return 'OK', 200
