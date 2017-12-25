import telebot


def __get_func(handlers, command):
    f = None
    for handler in handlers:
        commands = handler["filters"]["commands"]
        if command == None and commands == None:
            f = handler["function"]
            return f
        for com in commands:
            if com == command:
                f = handler["function"]
                return f
    return f


"""
:param bot: telegramBot
:param command: command from telegram
:param request_message: text from telegram
:param chat_id: chat id
"""
def test(bot, command, request_message, chat_id):
    f = __get_func(bot.message_handlers, command)
    if f == None:
        return None

    message = telebot.types.Message(None, None, None, None, None, [])
    message.text = request_message
    message.from_user = message.chat = telebot.types.Chat(chat_id, "private")
    res = f(message)
    return res
