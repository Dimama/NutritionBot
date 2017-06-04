import re
import datetime
import const
from dbhelper import DBHelper
from answerer import Answerer


class Handler(object):
    """ Класс для обработки сообщений пользователя"""

    @staticmethod
    def filter_request(message):
        """ Определение запроса пользователя из текста сообщения """

        if Handler.valid_text(const.reg_exp_dict["user data"], message.text):
            answer = Handler.set_update_user_data(message)
        elif Handler.valid_text(const.reg_exp_dict["product_by_name"], message.text):
            answer = Handler.add_product_by_name(message)
        elif Handler.valid_text(const.reg_exp_dict["product_by_id"], message.text):
            answer = Handler.add_product_by_id(message)
        elif Handler.valid_text(const.reg_exp_dict["day"], message.text):
            answer = Handler.stat_day(message)
        elif Handler.valid_text(const.reg_exp_dict["period"], message.text):
            answer = Handler.stat_period(message)
        else:
            answer = Answerer.unknow_command()
        return answer

    @staticmethod
    def valid_text(pattern, text):
        res = re.match(pattern, text)
        if res:
            return True
        return False

    @staticmethod
    def set_update_user_data(message):
        """ Метод для выделения данных пользователя из сообщения, их проверки и выполнения запроса к БД"""
        data = message.text.strip().split(',')
        try:
            sex = data[0].lower()
            age = int(data[1])
            height = int(data[2])
            weight = int(data[3])
        except ValueError:
            return Answerer.data_processing_error()

        if age > const.MAX_AGE:
            return Answerer.incorrect_data() + Answerer.max_age()

        if height > const.MAX_HEIGHT:
            return Answerer.incorrect_data() + Answerer.max_height()

        if weight > const.MAX_WEIGHT:
            return Answerer.incorrect_data() + Answerer.max_weight()

        data = {
            "id": message.chat.id,
            "first_name":  message.from_user.first_name,
            "second_name": message.from_user.last_name,
            "sex": sex,
            "age": age,
            "height": height,
            "weight": weight
        }

        db = DBHelper()
        answer = db.set_update_user_data(data)

        return answer

    @staticmethod
    def add_product_by_name(message):
        """ Метод для выделения данных о продукте, их проверки и выполнения запроса к БД"""
        data = message.text.strip().split(':')

        try:
            product = (data[0].strip()[0].upper() + data[0].strip()[1:])
            mass = int(data[1])
        except ValueError:
            return Answerer.data_processing_error()

        if mass > const.MAX_PRODUCT_MASS:
            return Answerer.incorrect_data() + Answerer.max_product_mass()

        data = {
            "id": message.chat.id,
            "product_name": product,
            "product_id": None,
            "mass": mass
        }
        db = DBHelper()
        answer = db.add_product(data)

        return answer

    @staticmethod
    def add_product_by_id(message):
        """ Метод для выделения данных о продукте, их проверки и выполнения запроса к БД"""
        data = message.text.strip().split(':')

        try:
            id = int(data[0][1:])
            mass = int(data[1])
        except ValueError:
            return Answerer.data_processing_error()

        if mass > const.MAX_PRODUCT_MASS:
            return Answerer.incorrect_data() + Answerer.max_product_mass()

        # Запрос к базе данных
        data = {
            "id": message.chat.id,
            "product_name": None,
            "product_id": id,
            "mass": mass
        }
        db = DBHelper()
        answer = db.add_product(data, by_id=True)

        return answer

    @staticmethod
    def is_correct_day(day, month, year):
        if day < 1 or day > 31 or month < 1 or month > 12:
            return False

        try:
            if datetime.date(year, month, day) > datetime.date.today():
                return False
        except ValueError:
            return False

        return True


    @staticmethod
    def stat_day(message):
        """ Метод для выделения даты из сообщения, ее проверки и выполнения запроса к БД """

        data = message.text.split('.')

        try:
            day = int(data[0])
            month = int(data[1])
            year = int(data[2])
        except ValueError:
            return Answerer.data_processing_error()

        if not Handler.is_correct_day(day, month, year):
            return Answerer.incorrect_date()

        data = {
            "id": message.from_user.id,
            "date": data[2] + "-" + data[1] + "-" + data[0]
        }

        db = DBHelper()
        answer = db.get_stat_day(data)
        return answer

    @staticmethod
    def stat_period(message):
        """ Метод для выделения интервала дат из сообщения, их проверки и выполнения запроса к БД """

        data = message.text.split('-')
        date1, date2 = data[0].split('.'), data[1].split('.')

        try:
            day1, day2 = int(date1[0]), int(date2[0])
            month1, month2 = int(date1[1]), int(date2[1])
            year1, year2 = int(date1[2]), int(date2[2])
        except ValueError:
            return Answerer.data_processing_error()

        if not Handler.is_correct_day(day1, month1, year1) or not Handler.is_correct_day(day2, month2, year2):
            return Answerer.incorrect_date()

        if not(datetime.date(year1, month1, day1) < datetime.date(year2, month2, day2)):
            return Answerer.incorrect_period()

        # Запрос к базе данных

        answer = "{0} - {1} - {2} :  {3} - {4} - {5}".format(day1, month1, year1, day2, month2, year2)

        return answer
