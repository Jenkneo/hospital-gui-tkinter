import psycopg2
import config
import datetime

# Когда-то давным-давно... Я не знал что такое ORM
# Я не знал как адекватно работать с базой данных через Python
# Поэтому раньше здесь были описаны огромнейшие SQL запросы к базе данных Postgres
# Сейчас этой базы давно нет в помине, а я даже не помню какие таблицы и поля там были
# Поэтому адаптировал функции, чтобы хоть как то запустить программу

# Старые SQL запросы в server_side_old.py


def LOGIN_WORKER(login, password):
        user = {
            "ID": 1,
            "Name": 'Test',
            "Surname": 'Test',
            "Lastname": 'Test',
            "Post": 'Test',
            "Department": 'Test'
        }
        return user

def CHANGE_PASSWORD(executor, ID, password):
    return True


def GET_WORKERS(executor, ID = None):
    send_user_info=[]
    send_user_info.append({
        "ID": 2,
        "Name": 'Иван',
        "Surname": 'Иванов',
        "Lastname": 'Иванович',
        "Post": 'Администратор',
        "Department": 'Отдел закупок',
        "Login": 'vanya'})

    send_user_info.append({
        "ID": 3,
        "Name": 'Александр',
        "Surname": 'Александров',
        "Lastname": 'Александрович',
        "Post": 'Стажер',
        "Department": 'Отдел коронавирус',
        "Login": 'vanya'})

    return(send_user_info)


def CREATE_NEW_WORKER(executor, Name, Surname, Lastname, Post, Department, Login, Password):
    return True

def GET_LOGS(id=0):
    send_info = []
    send_info.append({
        "Initiator": 'Он',
        "Date": '12.12.2023',
        "Time": '23:59:59',
        "Event": 'Записал',
        "End_user": 'Его'
        })
    return (send_info)

def LOAD_NEWS():
    return None


def DELETE_WORKER(executor, ID, name, surname):
    return True


def CHANGE_WORKERDATA(executor, ID, name, surname, lastname, department, post):
    return True


def GET_DOCTORS(executor, ID = None):
    send_user_info=[]
    send_user_info.append({
        "ID": 4,
        "Name": 'Михаил',
        "Surname": 'Михайлов',
        "Lastname": 'Михайлович',
        "Profile": "Офтальмолог",
        "Workdays": 1,
        "Workhours": '23:59:59'
    })
    send_user_info.append({
        "ID": 5,
        "Name": 'Алексей',
        "Surname": 'Алексеев',
        "Lastname": 'Алексеевич',
        "Profile": "Педиатр",
        "Workdays": 2,
        "Workhours": '23:59:59'
    })
    return(send_user_info)


def GET_CLIENTS(executor, ID = None):

    send_user_info=[]
    send_user_info.append({
            "ID": 6,
            "Name": 'Ирина',
            "Surname": 'Иринова',
            "Lastname": 'Ириновна',
            "Address": 'Ул.Пушкина д.Колотушкина',
            "MedicalID": 12345678,
            "Phone": 88005553535
        })
    return(send_user_info)

#Testing
if __name__ == "__main__":
    print(LOGIN_WORKER("root", "root"))


