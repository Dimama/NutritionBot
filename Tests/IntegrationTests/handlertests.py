import sys
from const import *
import unittest
from handler import Handler

# Входные данные и ожидаемые результаты
addUpdateUserData_in = [
    ["м,105,190,86", 376468900, "Дмитрий", "Мельников"],
    ["м,20,190,500", 376468900, "Дмитрий", "Мельников"],
    ["м,20,300,86", 376468900, "Дмитрий", "Мельников"],
    ["м,20,190,87", 159263487, "Дмитрий", "Иванов"],
    ["м,20,190,87", 376468900, "Дмитрий", "Мельников"]
]
addUpdateUserData_out = [
    error_emoji + " Введены некорректные данные.\n" + "Максимальный возраст: {0}".format(MAX_AGE),
    error_emoji + " Введены некорректные данные.\n" + "Максимальный вес: {0} кг".format(MAX_WEIGHT),
    error_emoji + " Введены некорректные данные.\n" + "Максимальный рост: {0} см".format(MAX_HEIGHT),
    success_emoji + " Данные успешно добавлены.",
    success_emoji + " Данные успешно обновлены."
]

addProductByName_in  = [
    ["творог 5%: 11000", 376468900],
    ["творог 5%: 587", 100100100],
    ["лобстер: 400", 376468900],
    ["Глинтвейн: 150", 376468900],
    ["творог 5%: 250 ", 376468900]
]
addProductByName_out = [
    error_emoji + " Введены некорректные данные.\n" + "Максимальная масса продукта: 10000 грамм",
    pencil_emoji + " Введите персональные данные!",
    sad_emoji + " К сожалению, такого продукта нет в базе. Проверьте правильность написания",
    sad_emoji + " К сожалению, такого продукта нет в базе.\n" \
                 "Возможно, Вы имели в виду:" \
                 "\n *319 - Глинтвейн August Weinxof" \
                 "\n *320 - Глинтвейн St Lorenz" \
                 "\n----------------\nВведите инофрмацию о продукте в формате:\n*номер : масса(грамм)",
    success_emoji + " Данные успешно добавлены."
]

addProductById_in  = [
    ["*774: 11000", 376468900],
    ["*774: 587", 100100100],
    ["*9989: 275", 376468900],
    ["*774: 275", 376468900],
]
addProductById_out = [
    error_emoji + " Введены некорректные данные.\n" + "Максимальная масса продукта: 10000 грамм",
    pencil_emoji + " Введите персональные данные!",
    sad_emoji + " Продукт с таким номером не найден.",
    success_emoji + " Данные успешно добавлены.",
]

class TestHandler(unittest.TestCase):
    def testAddUpdateUserData(self):
        for i in range(len(addUpdateUserData_in)):
            with self.subTest(text=addUpdateUserData_in[i]):
                text = addUpdateUserData_in[i][0]
                _id = addUpdateUserData_in[i][1]
                first_name = addUpdateUserData_in[i][2]
                last_name = addUpdateUserData_in[i][3]
                self.assertEqual(Handler.set_update_user_data(text, _id, first_name, last_name),
                                 addUpdateUserData_out[i])

    def testAddProductByName(self):
        for i in range(len(addProductByName_in)):
            with self.subTest(text=addProductByName_in[i]):
                text = addProductByName_in[i][0]
                _id = addProductByName_in[i][1]
                self.assertEqual(Handler.add_product_by_name(text, _id),
                                 addProductByName_out[i])

    def testAddProductById(self):
        for i in range(len(addProductById_in)):
            with self.subTest(text=addProductById_in[i]):
                text = addProductById_in[i][0]
                _id = addProductById_in[i][1]
                self.assertEqual(Handler.add_product_by_id(text, _id),
                                 addProductById_out[i])



if __name__ == "__main__":
    unittest.main()