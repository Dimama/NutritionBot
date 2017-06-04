from config import mail
import const


class Answerer(object):
    """ Класс, отвечающий за формирование текстовых ответов на сообщения пользователя"""

    @staticmethod
    def no_product():
        return const.sad_emoji + " К сожалению, такого продукта нет в базе. Проверьте правильность написания"

    @staticmethod
    def no_product_id():
        return const.sad_emoji + " Продукт с таким номером не найден."

    @staticmethod
    def similar_products(products):
        answer = const.sad_emoji + " К сожалению, такого продукта нет в базе.\n" \
                 "Возможно Вы имели в виду:"

        for product in products:
            answer += "\n *" + str(product[0]) + " - " + product[1]
        answer += "\n----------------\nВведите инофрмацию о продукте в формате:\n*номер : масса(грамм)"

        return answer

    @staticmethod
    def bot_info():
        """ Обработка команды 'Помощь' """
        answer = "NutritionBot хранит информацию о съеденной вами пище, рассчитывает полученные килокалории," \
                 " белки, жиры, углеводы и сравнивает с оптимальными для вас показателями." \
                 "\n------------------------------------------------" \
                 "\nДля работы нужно:" \
                 "\n1. Один раз отправить боту информацию о себе в формате:\nпол(м/ж), возраст, рост(см), вес(кг)" \
                 "\nПри необходимости (изменение веса и т.д.) введите информацию в том же формате ещё раз, " \
                 "бот запомнит новые данные." \
                 "\n2. Записывать съеденные продукты в формате:\nпродукт: масса(грамм)\nили" \
                 "\n*номер: масса(грамм)" \
                 "\n------------------------------------------------" \
                 "\nЧтобы посмотреть статистику за день, введите дату в формате: \nДД.ММ.ГГГГ" \
                 "\nЧтобы увидеть статистику за период, введите период в формате: \nДД.ММ.ГГГГ-ДД.ММ.ГГГГ" \
                 "\nДля повторного вывода данной инструкции нажмите 'Помощь'." \
                 "\nДля получения информации о команде нажмите на соответствующую кнопку меню." \
                 "\n------------------------------------------------" \
                 "\nКонтактная информация: " + mail

        return answer

    @staticmethod
    def add_product_info():
        """ Обработка команды  'Добавить продукт' """
        return "Введите информацию в формате:\n" \
                "продукт: масса(грамм)\n" \
                "или\n" \
                "*номер : масса(грамм)"


    @staticmethod
    def stat_by_day_info():
        """ Обработка команды 'Статистика за день' """
        return "Введите день в формате: \n" \
                "ДД.ММ.ГГГГ"


    @staticmethod
    def stat_by_period_info():
        """ Обработка команды 'Статистика за период' """
        return "Введите период в формате: \n" \
                "ДД.ММ.ГГГГ-ДД.ММ.ГГГГ"

    @staticmethod
    def set_update_data_info():
        """ Обработка команды 'Ввести/обновить личные данные' """
        return "Введите данные в формате: \n" \
                "пол(м/ж), возраст, рост(см), вес(кг)"


    @staticmethod
    def unknow_command():
        return "Я не знаю такой команды " + const.sad_emoji + "\n" \
                "Нажмите 'Помощь' для получения всей информации.\n" \
                "Для получения информации о команде нажмите на соответствующую кнопку меню."

    @staticmethod
    def data_processing_error():
        return const.error_emoji + " Ошибка обработки данных. Повторите ввод."

    @staticmethod
    def incorrect_date():
        return const.error_emoji + " Введена некорректная дата."

    @staticmethod
    def incorrect_period():
        return const.error_emoji + " Введен некорректный период."

    @staticmethod
    def incorrect_data():
        return const.error_emoji + " Введены некорректные данные.\n" \

    @staticmethod
    def max_age():
        return "Максимальный возраст: {0}".format(const.MAX_AGE)

    @staticmethod
    def max_height():
        return "Максимальный рост: {0} см".format(const.MAX_HEIGHT)

    @staticmethod
    def max_weight():
        return Answerer.incorrect_data() + "Максимальный вес: {0} кг".format(const.MAX_WEIGHT)

    @staticmethod
    def max_product_mass():
        return "Максимальная масса продукта: {0} грамм".format(const.MAX_PRODUCT_MASS)

    @staticmethod
    def db_error():
        return "Возникла ошибка при добавлении данных. Повторите ввод."

    @staticmethod
    def success_adding():
        return const.success_emoji + " Данные успешно добавлены."

    @staticmethod
    def success_updating():
        return const.success_emoji + " Данные успешно обновлены."

    @staticmethod
    def no_user_data():
        return const.pencil_emoji + " Введите персональные данные!"
