import sqlite3

# Підключення до бази даних (створення, якщо не існує)
conn = sqlite3.connect('weather.bd')
c = conn.cursor()

# Створення таблиці, якщо не існує
c.execute('''
    CREATE TABLE IF NOT EXISTS weather (
        date_time TEXT,
        temperature REAL
    )
''')

conn.commit()
conn.close()
