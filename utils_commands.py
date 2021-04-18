from utils import get_full_name


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