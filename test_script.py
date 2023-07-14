from telegram import Bot

# Telegram bot token
BOT_TOKEN = '6135924880:AAH7jJQtLpnyTENBTqeAdgDMBtzbvaK07vw'

# Message to send
message = 'Hello from the test script!'

# Function to send the message
def send_message():
    bot = Bot(token=BOT_TOKEN)
    bot.send_message(chat_id='YOUR_CHAT_ID', text=message)

# Call the send_message function
send_message()
