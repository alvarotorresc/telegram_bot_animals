from telegram.ext import Updater, CommandHandler
import requests
import re
from animals.dog import dog_image, dog_video
from animals.cat import cat_image, cat_video
import logging
import os
from env import TELEGRAM_BOT_TOKEN

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def main():
    print("Bot started...")
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('dogimage',dog_image))
    dp.add_handler(CommandHandler('dogvideo',dog_video))
    dp.add_handler(CommandHandler('catimage',cat_image))
    dp.add_handler(CommandHandler('catvideo',cat_video))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()