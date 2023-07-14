from flask import Flask
import schedule
import time
from telegram import Bot

app = Flask(__name__)

# Telegram bot token
BOT_TOKEN = '6135924880:AAH7jJQtLpnyTENBTqeAdgDMBtzbvaK07vw'

# URL to be posted
URL = 'https://www.9987up.cc/#/register?r_code=3272217765'

# Function to post the URL to groups
def post_url_to_groups():
    bot = Bot(token=BOT_TOKEN)
    groups = bot.get_updates()

    for group in groups:
        chat_id = group.effective_chat.id
        bot.send_message(chat_id=chat_id, text=URL)

# Schedule the URL posting every 3 minutes
schedule.every(3).minutes.do(post_url_to_groups)

# Run the bot
while True:
    schedule.run_pending()
    time.sleep(1)



@app.route('/')
def hello_world():
    return 'Welcome To Nia Chatbot basic'


if __name__ == "__main__":
    app.run()
