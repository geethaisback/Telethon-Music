import schedule
from telegram import Bot
from config import Config


def callback_auto_message(context):
    bot = Bot(token=Config.BOT_TOKEN)
    group_id = 'publictestbottc'
    message = 'Automatic message!'
    bot.send_message(chat_id=group_id, text=message)

def start_auto_messaging(update, context):
    chat_id = update.message.chat_id
    context.job_queue.run_repeating(callback_auto_message, interval=60, context=chat_id, name=str(chat_id))
    # context.job_queue.run_once(callback_auto_message, 3600, context=chat_id)
    # context.job_queue.run_daily(callback_auto_message, time=datetime.time(hour=9, minute=22), days=(0, 1, 2, 3, 4, 5, 6), context=chat_id)

def stop_notify(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text='Stopping automatic messages!')
    job = context.job_queue.get_jobs_by_name(str(chat_id))
    job[0].schedule_removal()
