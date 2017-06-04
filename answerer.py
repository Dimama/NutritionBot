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
    def no_product_at_day():
        return "За этот день информация о съеденной пище отсутствует."

    @staticmethod
    def no_product_at_period():
        return "За этот период информация о съеденной пище отсутствует."

    @staticmethod
    def similar_products(products):
        answer = const.sad_emoji + " К сожалению, такого продукта нет в базе.\n" \
                 "Возможно, Вы имели в виду:"

        for product in products:
            answer += "\n *" + str(product[0]) + " - " + product[1]
        answer += "\n----------------\nВведите инофрмацию о продукте в формате:\n*номер : масса(грамм)"

        return answer

    @staticmethod
    def stat_by_day(products, sum_energy, bx):
        """ Выдача статистики за день"""
        answer = "Съеденные продукты:"
        for product in products:
            answer += " \n" + product[0] + " : " + str(product[1]) + " г"
        answer += "\n" + "-"*20
        answer += "\nВсего:" + "\nКкал: " + str(round(sum_energy[3], 1)) + "\nБелков(Б): " + str(round(sum_energy[0], 1)) \
                  + " г" + "\nЖиров(Ж): " + str(round(sum_energy[1], 1)) \
                  + " г" + "\nУглеводов(У): " + str(round(sum_energy[2], 1)) + " г"
        answer += "\n" + "-" * 20

        calories = list(map(lambda x: str(round(x, 1)), bx["calories"]))
        protein = list(map(lambda x: str(round(x, 1)), bx["protein"]))
        fat = list(map(lambda x: str(round(x, 1)), bx["fat"]))
        carbs = list(map(lambda x: str(round(x, 1)), bx["carbs"]))

        answer += "\nРекомендованные для Вас нормы в зависимости от уровня физ. активности\n"
        answer += "              Ккал   Б(г)   Ж(г)   У(г)"
        answer += "\n " + const.moon_emoji + const.sleep_emoji + "  " +\
                   calories[0] + " | " + protein[0] + " | " + fat[0] + " | " + carbs[0]
        answer += "\n " + const.study_emoji + const.computer_emoji + "  " +\
                  calories[1] + " | " + protein[1] + " | " + fat[1] + " | " + carbs[1]
        answer += "\n " + const.policeman_emoji + const.haircut_emoji + "  " +\
                  calories[2] + " | " + protein[2] + " | " + fat[2] + " | " + carbs[2]
        answer += "\n " + const.tractor_emoji + const.wrench_emoji + "  " +\
                  calories[3] + " | " + protein[3] + " | " + fat[3] + " | " + carbs[3]
        answer += "\n " + const.biceps_emoji + const.bycyclist_emoji + "  " +\
                  calories[4] + " | " + protein[4] + " | " + fat[4] + " | " + carbs[4]
        return answer

    @staticmethod
    def stat_by_period(days):
        answer = ""
        if len(days) > 100:
            answer += "Показаны последние 100 дней\n"
            days = days[-100:]
        answer += const.diagram_emoji + " Статистика за период " + const.calendar_emoji\
                  + "\nДата:\nКкал | Белки(г) | Жиры(г) | Углеводы(г)"
        for day in days:
            nums = day[0].split('-')
            answer += "\n" + nums[2] + "." + nums[1] + "." + nums[0][2:] + ":\n" + str(round(day[4], 1)) + " | " + \
                      str(round(day[1], 1)) + " | " + str(round(day[2], 1)) + " | " + str(round(day[3], 1))
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
        return const.error_emoji + " Введены некорректные данные.\n"

    @staticmethod
    def max_age():
        return "Максимальный возраст: {0}".format(const.MAX_AGE)

    @staticmethod
    def max_height():
        return "Максимальный рост: {0} см".format(const.MAX_HEIGHT)

    @staticmethod
    def max_weight():
        return "Максимальный вес: {0} кг".format(const.MAX_WEIGHT)

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
