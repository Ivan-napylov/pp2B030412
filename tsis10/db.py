import psycopg2

# Подключение к базе данных
with psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="admin",
    host="127.0.0.1"
) as conn:

    # Создание курсора для выполнения операций в базе данных
    cur = conn.cursor()

    query_for_insert_data = '''INSERT INTO PhoneBook (name, phone_number) VALUES (%s, %s)'''


    print("Отправьте 1 если вы хотите посмотреть всю телефонную книгу")
    print("Отправьте 2 для записи")
    print("Отправьте 3 для изменения")
    print("Отправьте 4 для удаления")
    print("Отправьте 5 для добавления данных из csv файла")
    print("Отправьте 0 для выхода")

    run = True

    while run:
        num = int(input())
        if num == 1:

            cur.execute("SELECT * FROM PhoneBook;")

            rows = cur.fetchall()
            print("|||  ID   |||         User name         |||         Phone number         |||")
            print("_________________________________________________________________________")
            print()
            for row in rows:
                print("|||   {0}   |||         {1}        |||         {2}         |||".format(row[0], row[1], row[2]))
                print("_________________________________________________________________________")
                print()

            print("Чем ещё можем помочь?")
        elif num == 2:
            name = input("Введите имя:       ")
            phone = input("Введите телефонный номер:      ")

            cur.execute(query_for_insert_data, (name, phone))
            conn.commit()

            print("Данные сохранены успешно")
            print("Чем ещё можем помочь?")
        elif num == 3:
            print("1 - Изменение по имени")
            print("2 - Изменение по телефону")

            change = int(input())

            if change == 2:
                phone = input("Введите телефонный номер:      ")
                name = input("Введите новое имя:       ")
                cur.execute('''UPDATE PhoneBook SET name = %s WHERE phone_number = %s;''', (name, phone))
                print("Данные сохранены успешно")
                print("Чем ещё можем помочь?")

            elif change == 1:
                name = input("Введите имя:       ")
                phone = input("Введите новый телефонный номер:      ")
                cur.execute('''UPDATE PhoneBook SET phone_number = %s WHERE name = %s;''', (phone, name))
                print("Данные сохранены успешно")
                print("Чем ещё можем помочь?")

            conn.commit()

        elif num == 0:
            run = False

        elif num == 4:
            print("Введите номер телефона и запись будет удалена")
            phone = input("Телефонный номер:      ")
            cur.execute("DELETE FROM PhoneBook WHERE phone_number = %s", (phone,))
            print("Данные изменены успешно")
            print("Чем ещё можем помочь?")

            conn.commit()
        elif num == 5:
            with open('file.csv', 'r') as f:
                cur.copy_from(f, 'PhoneBook', sep=',', columns=('name', 'phone_number'))
            print("Данные изменены успешно")
            print("Чем ещё можем помочь?")
            conn.commit()
