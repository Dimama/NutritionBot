import sys
from const import reg_exp_dict
import unittest
from handler import Handler

# Входные данные и ожидаемые результаты
addUpdateUserData_in = ["@,20, 180,80", "М, 2567, 180, 80", "М, 20, 180, 80, 19",
                        "ж, 10, 20 ", "ж, 18, 160, 50", "  Ж,   20, 160, 55     "]
addUpdateUserData_out = [False, False, False, False, False, True]

addProductByName_in = ["Твор!ог: 150", "Курица: 1587076", "Яблоко: 75 896", "Творог","Творог 120",
                         "Творог :: 120", "Творог : 120", " Творог    :       120"]
addProductByName_out = [False, False, False, False, False, False, True, True]

addProductById_in = ["Курица: 155", "*1056: 1478964", "*1056: 1457  966", "*155", "*1056 158",
                     "*1056 ! 122", "155: 900", "*157 : 150  ", "*157      :    150"]
addProductById_out = [False, False, False, False, False, False, False, True, True]

getStatByDay_in = ["12.july.2017", "1457.12.2014", "14.12.2014  10", "14.12",
                     "14 12.2014", "14.12.2014", "   14.12.2014      "]
getStatByDay_out = [False, False, False, False, False, True, True]

class TestRegExp(unittest.TestCase):
    def testAddUpdateUserData(self):
        for i in range(len(addUpdateUserData_in)):
            with self.subTest(text=addUpdateUserData_in[i]):
                self.assertEqual(addUpdateUserData_out[i],
                                 Handler.valid_text(reg_exp_dict["user data"],
                                                    addUpdateUserData_in[i]))

    def testAddProductByName(self):
        for i in range(len(addProductByName_in)):
               with self.subTest(text=addProductByName_in[i]):
                    self.assertEqual(addProductByName_out[i],
                                 Handler.valid_text(reg_exp_dict["product_by_name"],
                                                    addProductByName_in[i]))

    def testAddProductById(self):
        for i in range(len(addProductById_in)):
               with self.subTest(text=addProductById_in[i]):
                    self.assertEqual(addProductById_out[i],
                                 Handler.valid_text(reg_exp_dict["product_by_id"],
                                                    addProductById_in[i]))

    def testGetStatByDay(self):
        for i in range(len(getStatByDay_in)):
               with self.subTest(text=getStatByDay_in[i]):
                    self.assertEqual(getStatByDay_out[i],
                                 Handler.valid_text(reg_exp_dict["day"],
                                                    getStatByDay_in[i]))


if __name__ == "__main__":
    unittest.main()