import unittest
from main import bot
from Tests.SystemTests.tests import test
from const import *


class TestSystem(unittest.TestCase):

        def testInputOrUpdateUserData(self):
            chat_id = 168115976
            res = test(bot, None, "Ввести/Обновить личные данные", chat_id)
            check_text = 'Введите данные в формате: \nпол(м/ж), возраст, рост(см), вес(кг)'
            self.assertEqual(res.text, check_text)

        def testInputProduct(self):
            chat_id = 168115976
            res = test(bot, None, "курица: 150", chat_id)
            check_text = sad_emoji + " К сожалению, такого продукта нет в базе.\n"\
                                    "Возможно, Вы имели в виду:\n"\
                                    " *761 - Курица (грудка вареная)\n"\
                                    " *762 - Курица (грудка копченая)\n"\
                                    " *763 - Курица (грудка на пару)\n"\
                                    " *764 - Курица (грудка)\n"\
                                    " *765 - Курица (желудки)\n"\
                                    " *766 - Курица (крылышки)\n"\
                                    " *767 - Курица (окорочка)\n"\
                                    " *768 - Курица (печень вареная)\n"\
                                    " *769 - Курица (печень жареная)\n"\
                                    " *770 - Курица (печень)\n"\
                                    " *771 - Курица (сердце вареное)\n"\
                                    " *772 - Курица (сердце)\n"\
                                    " *773 - Курица (филе вареное)\n"\
                                    " *774 - Курица (филе)\n"\
                                    " *775 - Курица вареная\n"\
                                    " *776 - Курица жареная\n"\
                                    "----------------\n"\
                                    "Введите инофрмацию о продукте в формате:\n"\
                                    "*номер : масса(грамм)"
            self.assertEqual(res.text, check_text)

        def testDate(self):
            chat_id = 168115976
            res = test(bot, None, "09.12.2020", chat_id)
            check_text = error_emoji + " Введена некорректная дата."
            self.assertEqual(res.text, check_text)

        def testPeriod(self):
            chat_id = 168115976
            res = test(bot, None, "10.02.2010 - 10.03.2010", chat_id)
            check_text = "За этот период информация о съеденной пище отсутствует."
            self.assertEqual(res.text, check_text)

        def testAddProduct(self):
            chat_id = 168115976
            res = test(bot, None, "Яблоко: 120", chat_id)
            check_text = success_emoji + " Данные успешно добавлены."
            self.assertEqual(res.text, check_text)

        def testUpdateAddUserData(self):
            chat_id = 168115976
            res = test(bot, None, "м, 199, 180, 90", chat_id)
            check_text = error_emoji + " Введены некорректные данные.\nМаксимальный возраст: {0}".format(MAX_AGE)
            self.assertEqual(res.text, check_text)

if __name__ == "__main__":
    unittest.main()
