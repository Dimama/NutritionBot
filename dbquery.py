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
