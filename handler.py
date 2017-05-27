import dbhelper
from config import mail
import const
import re
import telebot

class Handler(object):
    """ Класс для обработки сообщений пользователя"""

    @staticmethod
    def add_product_info():
        """ Обработка команды  'Добавить продукт' """
        answer = "Введите информацию в формате:\n" \
                 "продукт - масса(грамм)"
        return answer

    @staticmethod
    def instruction_info():
        """ Обработка команды 'Помощь' """
        answer = "NutritionBot, 2017  \n"\
                 "__________________\n" \
                 "Для получения информации об опции выберите соответсвующий пункт меню\n" \
                 "Контактная информация: " + mail
        return answer

    @staticmethod
    def stat_by_day_info():
        """ Обработка команды 'Статистика за день' """
        answer = "Введите день в формате: \n" \
                 "ДД.ММ.ГГГГ"
        return answer

    @staticmethod
    def stat_by_period_info():
        """ Обработка команды 'Статистика за период' """
        answer = "Введите период в формате: \n" \
                 "ДД.ММ.ГГГГ-ДД.ММ.ГГГГ"
        return answer

    @staticmethod
    def set_update_data_info():
        """ Обработка команды 'Ввести/обновить личные данные' """
        answer = "Введите данные в формате: \n" \
                 "пол(м/ж), возраст, рост(см), вес(кг)"
        return answer


    @staticmethod
    def filter_request(message):
        """ Определение запроса пользователя из текста сообщения """

        if Handler.valid_text(const.reg_exp_dict["user data"], message.text):
            answer = "True"
        elif Handler.valid_text(const.reg_exp_dict["product"], message.text):
            answer = "True"
        elif Handler.valid_text(const.reg_exp_dict["day"], message.text):
            answer = "True"
        elif Handler.valid_text(const.reg_exp_dict["period"], message.text):
            answer = "True"
        else:
            answer = "Я не знаю такой команды :("

        return answer

    @staticmethod
    def valid_text(pattern, text):
        res = re.match(pattern, text)
        if res:
            return True
        return False

