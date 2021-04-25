from telegram.ext import Updater, CommandHandler
from animals.dog import dog_image, dog_video
from animals.cat import cat_image, cat_video
import logging
import os
from utils_commands import help, start


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def main():
    print("Bot started...")
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    updater = Updater(token, use_context=True)
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