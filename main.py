from telegram.ext import Updater, CommandHandler
import requests
import re


def get_dog_url_image():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def dog(update, context):
    url = get_dog_url_image()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def main():
    print("Bot started...")
    updater = Updater('1768649263:AAHvQi3teNv7bkU6vOC5S8Swb9_TPn_qKVo', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('dog',dog))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()