import sqlite3
from dbconfig import DB_NAME, FILE_TABLE
import dbquery


class DBHelper(object):
    def __init__(self, dbname=DB_NAME):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):

        try:
            cursor = self.conn.cursor()
            products_data = DBHelper.load_table(FILE_TABLE)
            cursor.execute(dbquery.query_create_products_table)

            # записываем продукты в таблицу, только если она только что создана
            cursor.execute(dbquery.query_select_size_products)
            count_products = cursor.fetchone()[0]
            if count_products == 0:
                cursor.executemany(dbquery.query_insert_product_into_products, products_data)

            cursor.execute(dbquery.query_create_users_table)

        except sqlite3.DatabaseError as err:
            print("ERROR: ", err)
        else:
            self.conn.commit()

        self.conn.close()

    @staticmethod
    def load_table(filename):
        """ Считывание таблицы из файла и формирование списка кортежей"""
        table = []
        with open(filename, "r", encoding='utf-8') as f:
            for line in f.readlines():
                line = line.replace("\n", "")
                product = line.split('\t')
                table.append((product[0], float(product[1]), float(product[2]), float(product[3]), float(product[4])))
        return table

    def add_product(self, data):
        pass

    def get_stat_day(self, data):
        pass

    def get_stat_period(self, data):
        pass

    def set_update_user_data(self, data):
        try:
            cursor = self.conn.cursor()

            # проверить наличие записи
            cursor.execute(dbquery.query_select_user, (data["id"], ))
            if cursor.fetchone():

                cursor.execute(dbquery.query_update_user,
                               (data["sex"], data["age"], data["height"], data["weight"], data["id"]))
                answer = "Данные успешно обновлены."

            else:
                cursor.execute(dbquery.query_add_user, (data["id"], data["first_name"], data["second_name"],
                                                        data["sex"], data["age"], data["height"], data["weight"]))
                cursor.execute(dbquery.query_create_user_journal % ("journal_" + str(data["id"])))
                answer = "Данные успешно добавлены."

        except sqlite3.DatabaseError as err:
            print("ERROR: ", err)
            answer = "Возникла ошибка при добавлении данных. Повторите ввод."
        else:
            self.conn.commit()

        self.conn.close()
        return answer
