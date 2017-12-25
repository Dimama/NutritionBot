from config import token
import telebot
import const
from handler import Handler
import dbhelper
from answerer import Answerer
import traceback
import time

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def handle_command(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    user_markup.row('Статистика за день', 'за период')
    user_markup.row('Добавить продукт')
    user_markup.row('Ввести/Обновить личные данные')
    user_markup.row('Помощь')
    return bot.send_message(message.from_user.id, Answerer.bot_info(), reply_markup=user_markup)




@bot.message_handler()
def handle_command(message):
    print(type(message))
    if message.text in const.info_dict.keys():
        handler = const.info_dict.get(message.text)
        answer = handler()
    else:
        answer = Handler.filter_request(message)

    print(message)
    print(message.text)
    return bot.send_message(message.chat.id, answer)


def telegram_polling():
    try:
        db = dbhelper.DBHelper()
        db.setup()
        bot.polling(none_stop=True, interval=0)
    except:
        traceback_error_string = traceback.format_exc()
        with open("Error.Log", "a") as myfile:
            myfile.write("\r\n\r\n" + time.strftime(
                "%c") + "\r\n<<ERROR polling>>\r\n" + traceback_error_string + "\r\n<<ERROR polling>>")
        bot.stop_polling()
        time.sleep(10)
        telegram_polling()

def main():
    db = dbhelper.DBHelper()
    db.setup()
    bot.polling(none_stop=True, interval=0)
    #telegram_polling()

if __name__ == "__main__":
    main()