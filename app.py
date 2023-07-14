from flask import Flask
import schedule
import time
from telegram import Bot

app = Flask(__name__)

# Function to send the specific message to each group
def send_specific_message_to_groups():
    bot_token = '6135924880:AAH7jJQtLpnyTENBTqeAdgDMBtzbvaK07vw'
    message = 'Hello Everyone 👋🏻'

    bot = telegram.Bot(token=bot_token)
    groups = bot.getUpdates()  # Retrieve information about the groups the bot is a member of

    for group in groups:
        chat_id = group.effective_chat.id
        bot.send_message(chat_id=chat_id, text=message)

# Schedule the message to be sent every hour
schedule.every(1).minutes.do(send_specific_message_to_groups)

# Run the timer
while True:
    schedule.run_pending()
    time.sleep(1)


@app.route('/')
def hello_world():
    return 'Welcome To Nia Chatbot basic'


if __name__ == "__main__":
    app.run()
