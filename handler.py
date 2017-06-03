from config import mail
import re
import datetime
import const
import dbhelper


class Handler(object):
    """ Класс для обработки сообщений пользователя"""

    @staticmethod
    def add_product_info():
        """ Обработка команды  'Добавить продукт' """
        answer = "Введите информацию в формате:\n" \
                 "продукт : масса(грамм)"
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
            answer = Handler.set_update_user_data(message)
        elif Handler.valid_text(const.reg_exp_dict["product"], message.text):
            answer = Handler.add_product(message)
        elif Handler.valid_text(const.reg_exp_dict["day"], message.text):
            answer = Handler.stat_day(message)
        elif Handler.valid_text(const.reg_exp_dict["period"], message.text):
            answer = Handler.stat_period(message)
        else:
            answer = "Я не знаю такой команды :("

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
            return const.error_emoji + " Ошибка обработки данных. Повторите ввод."

        if age > const.MAX_AGE:
            return const.error_emoji + " Введены некорректные данные.\n" \
                                       "Максимальный возраст: {0}".format(const.MAX_AGE)

        if height > const.MAX_HEIGHT:
            return const.error_emoji + " Введены некорректные данные.\n" \
                     "Максимальный рост: {0} см".format(const.MAX_HEIGHT)

        if weight > const.MAX_WEIGHT:
            return const.error_emoji + " Введены некорректные данные.\n" \
                     "Максимальный вес: {0} кг".format(const.MAX_WEIGHT)

        # Запрос к базе данных

        data = {
            "id": message.chat.id,
            "first_name":  message.from_user.first_name,
            "second_name": message.from_user.last_name,
            "sex": sex,
            "age": age,
            "height": height,
            "weight": weight
        }

        db = dbhelper.DBHelper()
        answer = db.set_update_user_data(data)

        return answer

    @staticmethod
    def add_product(message):
        """ Метод для выделения данных о продукте, их проверки и выполнения запроса к БД"""
        data = message.text.strip().split(':')

        try:
            product = data[0].strip()
            mass = int(data[1])
        except ValueError:
            return const.error_emoji + " Ошибка обработки данных. Повторите ввод."

        if mass > const.MAX_PRODUCT_MASS:
            return const.error_emoji + " Введены некорректные данные.\n" \
                     "Максимальная масса продукта: {0} грамм".format(const.MAX_PRODUCT_MASS)

        # Запрос к базе данных

        answer = "Продукт: {0}, масса: {1}".format(product, mass)

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
            return const.error_emoji + " Ошибка обработки данных. Повторите ввод."

        if not Handler.is_correct_day(day, month, year):
            return const.error_emoji + " Введена некорректная дата."

        # Запрос к базе данных

        answer = "{0} - {1} - {2}".format(day, month, year)

        return answer

    @staticmethod
    def stat_period(message):
        """ Метод для выделения интервала дат из сообщения, его проверки и выполнения запроса к БД """

        data = message.text.split('-')
        date1, date2 = data[0].split('.'), data[1].split('.')

        try:
            day1, day2 = int(date1[0]), int(date2[0])
            month1, month2 = int(date1[1]), int(date2[1])
            year1, year2 = int(date1[2]), int(date2[2])
        except ValueError:
            return const.error_emoji + " Ошибка обработки данных. Повторите ввод."

        if not Handler.is_correct_day(day1, month1, year1) or not Handler.is_correct_day(day2, month2, year2):
            return const.error_emoji + " Введена некорректная дата."

        if not(datetime.date(year1, month1, day1) < datetime.date(year2, month2, day2)):
            return const.error_emoji + " Введен некорректный период."

        # Запрос к базе данных

        answer = "{0} - {1} - {2} :  {3} - {4} - {5}".format(day1, month1, year1, day2, month2, year2)

        return answer
