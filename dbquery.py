""" ЗАПРОСЫ К БД"""

create_products_table = """CREATE TABLE IF NOT EXISTS 
                                    Products (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        product TEXT,
                                        protein REAL,
                                        fat REAL,
                                        carbs REAL,
                                        calories REAL )"""

create_users_table = """CREATE TABLE IF NOT EXISTS
                                Users (
                                    id INTEGER PRIMARY KEY NOT NULL,
                                    first_name TEXT, last_name TEXT, sex TEXT, age INTEGER,
                                    height INTEGER, weight INTEGER 
                                    )"""

create_user_journal = """CREATE TABLE %s (datetime TEXT, product_id INTEGER,
                                                 mass INTEGER, protein REAL, fat REAL, carbs REAL, calories REAL,
                                                 FOREIGN KEY(product_id) REFERENCES Products(id))"""


select_size_products = """SELECT COUNT(*) FROM Products"""

select_user = """SELECT * FROM Users WHERE id = ?"""

select_product_info_by_name = """SELECT * FROM Products WHERE product = ?"""

select_product_info_by_id = """SELECT * FROM Products WHERE id = ?"""

select_all_products = """SELECT id, product FROM Products"""

select_products_by_day = """SELECT Products.product, mass
                                        FROM journal_%s INNER JOIN Products ON journal_%s.product_id = Products.id
                                        WHERE date(datetime) = ?"""

select_sum_energy_by_day = """SELECT SUM(protein), SUM(fat), SUM(carbs), SUM(calories)
                                        FROM journal_%s WHERE date(datetime) = ?"""

select_energy_by_period = """SELECT date(datetime), SUM(protein), SUM(fat), SUM(carbs), SUM(calories)
                            FROM journal_%s WHERE date(datetime) >= ? and date(datetime) <= ? GROUP BY date(datetime)"""


insert_product_into_products = """INSERT INTO Products Values(NULL, ?, ?, ?, ?, ?);"""

insert_product_into_journal_by_id = """INSERT INTO journal_%s Values(datetime('now', 'localtime'), ?, ?, ?, ?, ?, ?)"""

insert_product_into_journal_by_name = """INSERT INTO journal_%s Values(datetime('now', 'localtime'),
                                                    (SELECT id FROM Products WHERE product = ?), ?, ?, ?, ?, ?)"""

add_user = """ INSERT INTO Users Values(?, ?, ?, ?, ?, ?, ?);"""

update_user = """ UPDATE Users SET sex = ?, age = ?, height = ?, weight = ? WHERE id = ?"""






