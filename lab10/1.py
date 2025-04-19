import psycopg2
import json

# Устанавливаем соединение с PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="PhoneBook",
    user="madinazangirova",
    password="your_password"
)

def create_table():
    """Создание таблицы, если она не существует"""
    command = """
    CREATE TABLE IF NOT EXISTS phonebook (
        user_id SERIAL PRIMARY KEY,
        user_name VARCHAR(255) NOT NULL,
        user_phone VARCHAR(20) NOT NULL
    );
    """
    with conn.cursor() as cur:
        cur.execute(command)
        conn.commit()

# 1. Функция для поиска по шаблону
def search_by_pattern(pattern):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM phonebook WHERE user_name ILIKE %s OR user_phone ILIKE %s", (f"%{pattern}%", f"%{pattern}%"))
        rows = cur.fetchall()
        return rows

# 2. Процедура для добавления нового пользователя или обновления телефона
def insert_or_update_user(name, phone):
    with conn.cursor() as cur:
        cur.execute("""
        DO $$
        BEGIN
            IF EXISTS (SELECT 1 FROM phonebook WHERE user_name = %s) THEN
                UPDATE phonebook SET user_phone = %s WHERE user_name = %s;
            ELSE
                INSERT INTO phonebook (user_name, user_phone) VALUES (%s, %s);
            END IF;
        END
        $$;
        """, (name, phone, name, name, phone))
        conn.commit()

# 3. Процедура для вставки нескольких пользователей с проверкой правильности номера
def insert_multiple_users(users_list):
    with conn.cursor() as cur:
        for user in users_list:
            name = user['name']
            phone = user['phone']
            if phone.startswith('+'):  # Проверка правильности номера
                cur.execute("""
                DO $$
                BEGIN
                    IF EXISTS (SELECT 1 FROM phonebook WHERE user_name = %s) THEN
                        UPDATE phonebook SET user_phone = %s WHERE user_name = %s;
                    ELSE
                        INSERT INTO phonebook (user_name, user_phone) VALUES (%s, %s);
                    END IF;
                END
                $$;
                """, (name, phone, name, name, phone))
            else:
                print(f"Некорректный номер телефона для пользователя: {name}, телефон: {phone}")
        conn.commit()

# 4. Функция для получения данных с пагинацией
def get_phonebook_paginated(limit, offset):
    with conn.cursor() as cur:
        cur.execute("SELECT user_name, user_phone FROM phonebook LIMIT %s OFFSET %s", (limit, offset))
        rows = cur.fetchall()
        return rows

# 5. Процедура для удаления пользователя по имени или телефону
def delete_user(identifier):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM phonebook WHERE user_name = %s OR user_phone = %s", (identifier, identifier))
        conn.commit()

# Пример использования
def menu():
    while True:
        print("\nPHONEBOOK MENU")
        print("1 - Search by pattern")  # Поиск по шаблону
        print("2 - Insert or Update user")  # Вставка или обновление пользователя
        print("3 - Insert multiple users")  # Вставка нескольких пользователей
        print("4 - Get phonebook with pagination")  # Вывод с пагинацией
        print("5 - Delete user")  # Удаление пользователя
        print("6 - Exit")  # Выход
        choice = input("Choose option: ")
        
        if choice == '1':
            pattern = input("Enter search pattern: ")
            results = search_by_pattern(pattern)
            for row in results:
                print(row)
        elif choice == '2':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            insert_or_update_user(name, phone)
            print(f"User {name} with phone {phone} has been added or updated.")
        elif choice == '3':
            users_json = input("Enter users JSON: ")  # Пример: [{"name": "John Doe", "phone": "+9988776655"}, ...]
            users_list = json.loads(users_json)
            insert_multiple_users(users_list)
        elif choice == '4':
            limit = int(input("Enter limit: "))
            offset = int(input("Enter offset: "))
            results = get_phonebook_paginated(limit, offset)
            for row in results:
                print(row)
        elif choice == '5':
            identifier = input("Enter username or phone to delete: ")
            delete_user(identifier)
            print(f"User {identifier} has been deleted.")
        elif choice == '6':
            break
        else:
            print("Invalid option!")

# Основной процесс
create_table()
menu()

conn.close()
