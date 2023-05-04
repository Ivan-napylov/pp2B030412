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

    cur.execute('''CREATE TABLE SnakeScore (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    score INTEGER
);''')
    conn.commit()


