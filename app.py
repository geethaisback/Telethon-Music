from flask import Flask, request
import schedule
import time
import telegram

app = Flask(__name__)

bot_token = '6135924880:AAH7jJQtLpnyTENBTqeAdgDMBtzbvaK07vw'
bot = telegram.Bot(token=bot_token)

# Handler for the /run command
@app.route('/run', methods=['POST'])
def run_command():
    message = request.get_json()['message']
    command = message.get('text', '').lower()

    # Check if the command is /run
    if command == '/run':
        # Execute your desired functionality or code here
        # ...
        # Example: Send a response message
        chat_id = message['chat']['id']
        response = 'Running the script!'
        bot.send_message(chat_id=chat_id, text=response)

    return 'OK'


@app.route('/')
def hello_world():
    return 'Welcome To Nia Chatbot basic'


if __name__ == "__main__":
    app.run()
