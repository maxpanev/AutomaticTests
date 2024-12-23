import sqlite3

def init_db():
    # Создает соединение с базой данных в памяти (не на диске).
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    # Создает таблицу 'users', если она еще не существует, с полями id, name и age.
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER)
    ''')

    return conn  # Возвращает объект соединения с базой данных.

def add_user(conn, name, age):
    # Добавляет нового пользователя в таблицу 'users' с указанным именем и возрастом.
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO users (name, age) VALUES (?, ?)''', (name, age))
    conn.commit()  # Фиксирует изменения в базе данных.

def get_user(conn, name):
    # Извлекает пользователя из таблицы 'users' по имени.
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM users WHERE name = ?''', (name,))
    return cursor.fetchone()  # Возвращает первую найденную запись.