from flask import Flask
from telegram.ext import Updater, CommandHandler
import schedule
from telegram import Bot
from config import Config

app = Flask(__name__)

# Define your Flask routes and functions here
@app.route('/')
def hello_world():
    return 'Welcome To Nia Chatbot basic'

# Define the callback function for the automatic messaging
def callback_auto_message(context):
    bot = Bot(token=Config.BOT_TOKEN)
    group_id = 'publictestbottc'
    message = 'Automatic message!'
    bot.send_message(chat_id=group_id, text=message)

# Define the command handler for starting the automatic messaging
def start_auto_messaging(update, context):
    chat_id = update.message.chat_id
    context.job_queue.run_repeating(callback_auto_message, interval=60, context=chat_id, name=str(chat_id))
    # context.job_queue.run_once(callback_auto_message, 3600, context=chat_id)
    # context.job_queue.run_daily(callback_auto_message, time=datetime.time(hour=9, minute=22), days=(0, 1, 2, 3, 4, 5, 6), context=chat_id)

# Define the command handler for stopping the automatic messaging
def stop_notify(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text='Stopping automatic messages!')
    job = context.job_queue.get_jobs_by_name(str(chat_id))
    job[0].schedule_removal()

# Create the updater and dispatcher
updater = Updater(token=Config.BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Add command handlers
dispatcher.add_handler(CommandHandler("start_auto_messaging", start_auto_messaging))
dispatcher.add_handler(CommandHandler("stop_notify", stop_notify))

# Start the bot
updater.start_polling()

if __name__ == "__main__":
    app.run()
