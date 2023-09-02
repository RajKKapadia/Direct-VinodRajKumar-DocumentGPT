from flask import Flask, request

from document_gpt.helper.conversation import create_conversation
from document_gpt.helper.twilio_api import send_message

qa = create_conversation()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return 'OK', 200

@app.route('/twilio', methods=['POST'])
def twilio():
    query = request.form['Body']
    sender_id = request.form['From']
    print(sender_id, query)
    # TODO
    # get the user
    # if not create
    # create chat_history from the previous conversations
    # quetion and answer
    res = qa.run(query)

    print(res)
    
    send_message(sender_id, res)

    return 'OK', 200
