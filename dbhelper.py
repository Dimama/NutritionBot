import sqlite3
from dbconfig import DB_NAME, FILE_TABLE
import dbquery
from searchsimilar import SimilarSearcher
from answerer import Answerer
from calculator import Calculator


class DBHelper(object):
    def __init__(self, dbname=DB_NAME):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):

        try:
            cursor = self.conn.cursor()
            products_data = DBHelper.load_table(FILE_TABLE)
            cursor.execute(dbquery.create_products_table)

            # записываем продукты в таблицу, только если она только что создана
            cursor.execute(dbquery.select_size_products)
            count_products = cursor.fetchone()[0]
            if count_products == 0:
                cursor.executemany(dbquery.insert_product_into_products, products_data)

            cursor.execute(dbquery.create_users_table)

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

    def add_product(self, data, by_id=False):
        """ Добавление иформации о употребленном продукте в БД"""
        try:
            cursor = self.conn.cursor()

            cursor.execute(dbquery.select_user, (data["id"],))
            user = cursor.fetchone()
            if user:
                if by_id:
                    cursor.execute(dbquery.select_product_info_by_id, (data["product_id"],))
                    produсt = cursor.fetchone()
                    if produсt:
                        mass = data["mass"]
                        protein, fat, carbs, calories = Calculator.calc_product_energy(mass, produсt[2],
                                                                                produсt[3], produсt[4], produсt[5])
                        cursor.execute(dbquery.insert_product_into_journal_by_id % str(data["id"]),
                                       (data["product_id"], mass, protein, fat, carbs, calories))
                        answer = Answerer.success_adding()
                    else:
                        answer = Answerer.no_product_id()

                else:
                    cursor.execute(dbquery.select_product_info_by_name, (data["product_name"],))
                    produсt = cursor.fetchone()

                    if produсt:
                        mass = data["mass"]
                        protein, fat, carbs, calories = Calculator.calc_product_energy(mass, produсt[2], produсt[3],
                                                                                       produсt[4], produсt[5])
                        cursor.execute(dbquery.insert_product_into_journal_by_name % str(data["id"]),
                                       (data["product_name"], mass, protein, fat, carbs, calories))
                        answer = Answerer.success_adding()
                    else:
                        cursor.execute(dbquery.select_all_products)
                        produсts = cursor.fetchall()
                        searcher = SimilarSearcher(produсts)
                        sim_prod = searcher.search_similar(data["product_name"])
                        if sim_prod:
                            answer = Answerer.similar_products(sim_prod)
                        else:
                            answer = Answerer.no_product()
            else:
                answer = Answerer.no_user_data()

        except sqlite3.DatabaseError as err:
            print("ERROR: ", err)
            answer = Answerer.db_error()
        else:
            self.conn.commit()

        self.conn.close()
        return answer

    def set_update_user_data(self, data):
        """ Обновление/ добавление данных пользователя в БД"""
        try:
            cursor = self.conn.cursor()

            # проверить наличие записи
            cursor.execute(dbquery.select_user, (data["id"],))
            if cursor.fetchone():

                cursor.execute(dbquery.update_user,
                               (data["sex"], data["age"], data["height"], data["weight"], data["id"]))
                answer = Answerer.success_updating()

            else:
                cursor.execute(dbquery.add_user, (data["id"], data["first_name"], data["second_name"],
                                                  data["sex"], data["age"], data["height"], data["weight"]))
                cursor.execute(dbquery.create_user_journal % ("journal_" + str(data["id"])))
                answer = Answerer.success_adding()

        except sqlite3.DatabaseError as err:
            print("ERROR: ", err)
            answer = Answerer.db_error()
        else:
            self.conn.commit()

        self.conn.close()
        return answer

    def get_stat_day(self, data):
        """ Запрос к БД на получение статистики за день"""
        try:
            cursor = self.conn.cursor()

            cursor.execute(dbquery.select_user, (data["id"],))
            user = cursor.fetchone()
            if user:
                date = data["date"]
                id = str(data["id"])
                cursor.execute(dbquery.select_products_by_day % (id, id), (date, ))
                products = cursor.fetchall()
                if products:
                    cursor.execute(dbquery.select_sum_energy_by_day % id, (date,))
                    sum_energy = cursor.fetchone()
                    cl = Calculator(user[3], user[4], user[5], user[6])
                    bx = cl.calc_BX()
                    answer = Answerer.stat_by_day(products, sum_energy, bx)
                else:
                    answer = Answerer.no_product_at_day()
            else:
                answer = Answerer.no_user_data()

        except sqlite3.DatabaseError as err:
            print("ERROR: ", err)
            answer = Answerer.db_error()
        else:
            self.conn.commit()

        self.conn.close()
        return answer

    def get_stat_period(self, data):
        pass