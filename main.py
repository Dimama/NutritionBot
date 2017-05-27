from config import token
import telebot
import const
from handler import Handler

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def handle_command(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    user_markup.row('Статистика за день', 'за период')
    user_markup.row('Добавить продукт')
    user_markup.row('Ввести/Обновить личные данные')
    user_markup.row('Помощь')
    bot.send_message(message.from_user.id, "Список доступных команд", reply_markup=user_markup)


@bot.message_handler()
def handle_command(message):
    if message.text in const.info_dict.keys():
        handler = const.info_dict.get(message.text)
        answer = handler()
    else:
        answer = Handler.filter_request(message)
        #answer = "Я не знаю такой команды :("

    bot.send_message(message.chat.id, answer)


def main():
    bot.polling(none_stop=True, interval=0)

if __name__ == "__main__":
    main()