from telegram.ext import Updater, CommandHandler
import requests
import re
from animals.dog import dog_image, dog_video

def main():
    print("Bot started...")
    updater = Updater('1768649263:AAHvQi3teNv7bkU6vOC5S8Swb9_TPn_qKVo', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('dogimage',dog_image))
    dp.add_handler(CommandHandler('dogvideo',dog_video))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()