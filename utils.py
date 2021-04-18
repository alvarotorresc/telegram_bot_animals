def get_full_name(update):
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name

    return f"{first_name} {last_name}"