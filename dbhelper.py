import sqlite3
from const import DB_NAME, FILE_TABLE
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
            cursor.execute(dbquery.query_select_size_products)

            # записываем продукты в таблицу, только если она только что создана
            count_products = cursor.fetchone()[0]
            if count_products == 0:
                cursor.executemany(dbquery.query_insert_product_into_products, products_data)

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
        pass