import csv
import sqlite3
from tqdm import tqdm
import sys
import time
from loguru import logger


start = time.time()

sqlite_file = "db.sqlite3"
conn = sqlite3.connect(sqlite_file)
cursor = conn.cursor()


# запрос для создания таблицы
table_create = """
CREATE TABLE IF NOT EXISTS police_calls (
    'id' integer PRIMARY KEY,
    'Crime Id' integer,
    'Original Crime Type Name' integer,
    'Report Date' datetime,
    'Call Date' datetime,
    'Offense Date' datetime,
    'Call Time' datetime,
    'Call Date Time' datetime,
    'Disposition' varchar(100),
    'Address' varchar(100),
    'City' varchar(80),
    'State' varchar(80),
    'Agency Id' varchar(100),
    'Address Type' varchar(100),
    'Common Location' varchar(100)
)
"""

cursor.execute("drop table police_calls")
cursor.execute(table_create)

logger.remove()
logger.add(sys.stdout, format="{message}")
logger.add("file.log", format="{time} | {level} | {message}")

logger.success("[+] Таблица создана")


def insert_row(cursor, row):
    cursor.execute("insert into police_calls ('Crime Id', 'Original Crime Type Name', 'Report Date', 'Call Date', "
                   "'Offense Date', 'Call Time', 'Call Date Time', 'Disposition', 'Address', 'City', "
                   "'State', 'Agency Id', 'Address Type', 'Common Location') VALUES "
                   "(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)


with open("police-department-calls-for-service.csv") as log:
    csvreader = csv.reader(log, delimiter=',')
    start_inserting = time.time()

    for row_num, row in enumerate(tqdm(csvreader, bar_format="{elapsed} Обработано: {n_fmt}")):
        # игнорируем хидер
        if row_num != 0:
            insert_row(cursor, row)

    conn.commit()
    logger.success("[+] Данные записаны")

cursor.close()
conn.close()


logger.success("Время работы скрипта: {:8.4f}".format(time.time() - start))
logger.success("Время записи данных:  {:8.4f}".format(time.time() - start))


logger.success("------------------- done -------------------")
