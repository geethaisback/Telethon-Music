import schedule
import time
from telegram import Bot
from config import Config

# Function to send the message
def send_message():
    bot = Bot(token=Config.BOT_TOKEN)
    group_ids = ['@publictestbottc']  # Add your group IDs here
    message = 'Hello from the scheduled task!'
    for group_id in group_ids:
        bot.send_message(chat_id=group_id, text=message)

# Schedule the message to be sent every minute
schedule.every(1).minutes.do(send_message)

# Run the scheduler in a continuous loop
while True:
    schedule.run_pending()
    time.sleep(1)
