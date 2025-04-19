import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    host="localhost",
    database="PhoneBook",
    user="madinazangirova",
    password=""
)

def insert_or_update_user():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    with conn.cursor() as cur:
        cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
        conn.commit()
        print("User inserted or updated.")

def insert_many_users():
    names = []
    phones = []
    while True:
        entry = input("Enter name and phone separated by comma (or type 'done'): ")
        if entry.lower() == 'done':
            break
        try:
            name, phone = entry.split(',')
            names.append(name.strip())
            phones.append(phone.strip())
        except:
            print("Invalid format. Use: Name,Phone")

    with conn.cursor() as cur:
        cur.execute("CALL insert_many_users(%s, %s)", (names, phones))
        cur.execute("SELECT NULL")  # OUT-параметр можно обработать через DO-блок в SQL
        print("Bulk insert completed (check database for invalid entries).")
        conn.commit()

def search_by_pattern():
    pattern = input("Enter search pattern (part of name or phone): ")
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
        rows = cur.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No results found.")

def get_users_paginated():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM get_users_paginated(%s, %s)", (limit, offset))
        rows = cur.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No users found in this range.")

def delete_by_key():
    key = input("Enter name or phone to delete: ")
    with conn.cursor() as cur:
        cur.execute("CALL delete_user(%s)", (key,))
        conn.commit()
        print("User deleted if existed.")

def menu():
    while True:
        print("\nPHONEBOOK MENU")
        print("1 - Insert or update user")
        print("2 - Insert many users")
        print("3 - Search by pattern")
        print("4 - Paginated user list")
        print("5 - Delete by name or phone")
        print("6 - Exit")
        choice = input("Choose option: ")
        if choice == '1':
            insert_or_update_user()
        elif choice == '2':
            insert_many_users()
        elif choice == '3':
            search_by_pattern()
        elif choice == '4':
            get_users_paginated()
        elif choice == '5':
            delete_by_key()
        elif choice == '6':
            break
        else:
            print("Invalid option!")

# Запуск меню
menu()
conn.close()