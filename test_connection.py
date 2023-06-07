import psycopg2

host = "localhost"
user = "postgres"
password = "123Logout"
db_name = "users"
port = "5432"

def test_connection(host, port, user, password, db_name):
    try:
        connection = psycopg2.connect(
            host = host,
            port = port,
            user = user,
            password = password,
            database = db_name
        )

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT version();"
            )
            print (f"Server version: {cursor.fetchone()}")
            connection.close()
            return True
    except Exception as _ex:
        return False


# connection = psycopg2.connect(
#         host = host,
#         user = user,
#         password = password,
#         database = db_name
#     )


# cursor = connection.cursor()
# cursor.execute(
#     "INSERT INTO clients (name, surname, patronymic, passport, medical_card, address, phone) VALUES ('Фарадей', 'Мирей', 'Алексов', 12354679, 987654321, 'Ул.Моисеевская 13 д 11',79608557896)"
# )
# connection.commit()

# cursor.execute("SELECT * FROM clients where ID = 1")
# resilts = cursor.fetchall()
# print (resilts)

print("Здравствуйте! Вас приветствует мастер настройки базы данных для приложения \'Медицинские услуги. Регистратура\'")
print("Для продолжения, выберите, каким способом вы хотите указать данные для подключения?")
print("1 - Ввести данные вручную")
print("2 - Получить данные из файла db_config.txt")
ask = input("Выбор: ")

if ask == "1":
    host = input("host[localhost]: ")
    db_name = input("Database[postgres]: ")
    port = input("port[5432]: ")
    user = input("user[postgres]: ")
    password = input("Пароль пользователя " + user + ": ")

    if host == "": host = "localhost"
    if db_name == "": db_name = "postgres"
    if port == "": port = "5432"
    if user == "": user = "postgres"

elif ask == "2":
    ask2 = input("Данные для подключения к БД верны? [Y/N]: ")
    if ask2 != "Y" or ask2 != "y": pass
    elif ask2 == "N" or ask2 == "n":
        print("Внесите корректные данные в файл и перезапустите программу."); input(); exit()
    else:
        print("Неккоректный выбор."); input(); exit()
else:
    print("Неккоректный выбор."); input(); exit()

print("Производится тестовое подключение к базе данных...")
if test_connection(host, port, user, password, db_name):
    print("Проверка подключения к базе данных выполнена успешно!")
else:
    print("Подключиться к базе данных не удалось."); input(); exit()


print("Настройка аккаунта системного администратора.")
print("Логин root")
root_password = input("Введите новый пароль: ")

#check spaces*
#warning remeber password





# connection = psycopg2.connect(
#         host = host,
#         user = user,
#         password = password,
#         database = db_name
#     )


# cursor = connection.cursor()
# cursor.execute(
#     "INSERT INTO clients (name, surname, patronymic, passport, medical_card, address, phone) VALUES ('Фарадей', 'Мирей', 'Алексов', 12354679, 987654321, 'Ул.Моисеевская 13 д 11',79608557896)"
# )
# connection.commit()

# cursor.execute("SELECT * FROM clients where ID = 1")
# resilts = cursor.fetchall()
# print (resilts)

# create database hospital_registry;

# create table registry_workers(
#     ID       serial
#         constraint registry_workers_pk
#             primary key,
#     name     varchar(32)   not null,
#     surname  varchar(32)   not null,
#     patronymic varchar(32),
#     email    varchar(128),
#     login    varchar(32)   not null,
#     password varchar(256)  not null,
#     post     int default 1 not null
#     CHECK (post >0 AND post<1000)
# );
#
# create unique index registry_workers_email_uindex
#     on registry_workers (email);
#
# create unique index registry_workers_login_uindex
#     on registry_workers (login);


# INSERT INTO public.registry_workers (id, name, surname, patronymic, email, login, password, post)
# VALUES (DEFAULT, 'Алексей'::varchar(32), 'Невтюков'::varchar(32), 'Иванович'::varchar(32), 'root@mail.ru'::varchar(128),
#         'root'::varchar(32), md5('root')::varchar(256), 999::integer);


