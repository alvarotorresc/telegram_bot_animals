from telegram.ext import Updater, CommandHandler
import requests
import re
from animals.dog import dog_image, dog_video
from animals.cat import cat_image, cat_video
import logging
import os
from env import TELEGRAM_BOT_TOKEN
from utils import get_full_name

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def start(update, context):
    full_name = get_full_name(update)
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=(f"""Hello, {full_name}! \U0001F600""")
    )
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(""" Here you can see a list of available commands:

/dogimage   Show you a cute dog image 
/dogvideo    Show you a cute dog video
/catimage    Show you a cute cat image
/catvideo     Show you a cute cat video
/help            List of available commands
""")
    )

def help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(""" Here you can see a list of available commands:

/dogimage   Show you a cute dog image 
/dogvideo    Show you a cute dog video
/catimage    Show you a cute cat image
/catvideo     Show you a cute cat video
/help            List of available commands
""")
    )

def main():
    print("Bot started...")
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('dogimage',dog_image))
    dispatcher.add_handler(CommandHandler('dogvideo',dog_video))
    dispatcher.add_handler(CommandHandler('catimage',cat_image))
    dispatcher.add_handler(CommandHandler('catvideo',cat_video))
    dispatcher.add_handler(CommandHandler('help', help))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()