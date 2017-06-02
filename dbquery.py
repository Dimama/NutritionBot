""" ЗАПРОСЫ К БД"""

query_create_products_table = """CREATE TABLE IF NOT EXISTS 
                                    Products (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        product TEXT,
                                        protein REAL,
                                        fat REAL,
                                        carbs REAL,
                                        calories REAL )"""

query_select_size_products = """SELECT COUNT(*) FROM Products"""

query_insert_product_into_products = """INSERT INTO Products Values(NULL, ?, ?, ?, ?, ?);"""


query_create_users_table = """CREATE TABLE IF NOT EXISTS
                                Users (
                                    id INTEGER PRIMARY KEY NOT NULL,
                                    first_name TEXT, last_name TEXT, sex TEXT, age INTEGER,
                                    height INTEGER, weight INTEGER 
                                    )"""

query_add_user = """ INSERT INTO Users Values(?, ?, ?, ?, ?, ?, ?);"""

query_update_user = """ UPDATE Users SET sex = ?, age = ?, height = ?, weight = ? WHERE id = ?"""

query_select_user = """SELECT * FROM Users WHERE id = ?"""

query_create_user_journal = """CREATE TABLE %s (datetime TEXT, product_id INTEGER,
                                                 mass INTEGER, protein REAL, fat REAL, carbs REAL, calories REAL,
                                                 FOREIGN KEY(product_id) REFERENCES Products(id))"""
