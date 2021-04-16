import requests
import re

def get_dog_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_dog_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def get_video_url():
    allowed_extension = ['mp4','avi','gif']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_dog_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def dog_image(update, context):
    url = get_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def dog_video(update, context):
    url = get_video_url()
    chat_id = update.message.chat.id
    context.bot.send_video(chat_id, video=url)