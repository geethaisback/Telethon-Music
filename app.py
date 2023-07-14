from flask import Flask
import telegram
import schedule
import time

app = Flask(__name__)

# Telegram bot token
BOT_TOKEN = '6135924880:AAH7jJQtLpnyTENBTqeAdgDMBtzbvaK07vw'

# Message to send
message = 'Hello everyone'

# Function to send the message
def send_message():
    bot = Bot(token=BOT_TOKEN)
    groups = bot.get_updates()

    for group in groups:
        chat_id = group.effective_chat.id
        bot.send_message(chat_id=chat_id, text=message)

# Schedule the message to be sent every minute
schedule.every(1).minutes.do(send_message)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)


@app.route('/')
def hello_world():
    return 'Welcome To Nia Chatbot basic'


if __name__ == "__main__":
    app.run()
