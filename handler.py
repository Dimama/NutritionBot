import dbhelper
from config import mail


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
                 "ДД.ММ.ГГГГ : ДД.ММ.ГГГГ"
        return answer

    @staticmethod
    def set_update_data_info():
        """ Обработка команды 'Ввести/обновить личные данные' """
        answer = "Введите данные в формате: \n" \
                 "(пол(м/ж), возраст, рост, вес)"
        return answer