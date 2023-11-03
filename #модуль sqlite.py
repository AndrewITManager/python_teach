#модуль sqlite 
import sqlite3

DB_NAME = "sqlite_db.db"

# # CREATE DB
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     print(sqlite_conn)
#     print(sqlite3.version)

# # CREATE NEW TABLE
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = """CREATE TABLE IF NOT EXISTS courses (
#         id integer PRIMARY KEY,
#         title text NOT NULL,
#         students_qty integer,
#         reviews_qty integer
#     );"""

# sqlite_conn.execute(sql_request)


# # ADD RECORDS TO THE COURSES TABLE
# courses = [
#     (351, "JavaScript", 415, 100),
#     (614, "C++ course", 161, 10),
#     (721, "Java full course", 100, 35)
# ]

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
#     # sqlite_conn.execute(sql_request, (251, "Python course", 100, 30))
#     for course in courses:
#         sqlite_conn.execute(sql_request, course)
#     sqlite_conn.commit()

# # ВЫБОРКА ДАННЫХ ИЗ БАЗЫ ДАННЫХ
with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "SELECT * FROM courses WHERE reviews_qty>=30" #можно отфильтровать выборку
    sql_cursor = sqlite_conn.execute(sql_request)
    # for record in sql_cursor: #
    #     print(record[1])
    records = sql_cursor.fetchall()
    print(records)