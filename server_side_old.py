import psycopg2
import config
import datetime


def LOGIN_WORKER(login, password):
    try:
        connection = psycopg2.connect(
                host = config.host,
                user = config.user,
                password = config.password,
                database = config.db_name
            )
    except:
        return "db_err"
    cursor = connection.cursor()
    cursor.execute("SELECT ID, name, surname, lastname, post, department FROM workers where login = '" + login + "' and password = md5('" + password + "')")
    result = cursor.fetchall()
    connection.close()

    if len(result) == 0: return None
    elif len(result) == 1:
        result = list(result[0])
        if result[3] == None: result[3] = "<отсутствует>"
        user = {
            "ID":   result[0],
            "Name": result[1],
            "Surname": result[2],
            "Lastname": result[3],
            "Post": result[4],
            "Department": result[5]
        }
        return user

def CHANGE_PASSWORD(executor, ID, password):
    #executor to logs
    connection = psycopg2.connect(
        host=config.host,
        user=config.user,
        password=config.password,
        database=config.db_name
    )
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE workers SET password = md5('" + password + "')::varchar(256) WHERE id = "+ str(ID) +"::integer;"
    )
    connection.commit()

    cursor.execute(
        "SELECT name FROM workers where id = "+ str(ID) +" and password = md5('" + password + "') ;")
    result = cursor.fetchall()
    connection.close()
    if len(result) == 1: return True
    else: return False


def GET_WORKERS(executor, ID = None):
    connection = psycopg2.connect(
            host = config.host,
            user = config.user,
            password = config.password,
            database = config.db_name
        )

    cursor = connection.cursor()
    if ID != None:
        cursor.execute("SELECT ID, name, surname, lastname, post, department, login FROM workers WHERE id = '" + str(ID) + "'")
    elif executor == 1:
        cursor.execute("SELECT ID, name, surname, lastname, post, department, login FROM workers")
    else:
        cursor.execute("SELECT ID, name, surname, lastname, post, department, login FROM workers where post != 'root'")
    result = cursor.fetchall()
    connection.close()

    send_user_info=[]
    for user in result:
        edit_user_info = {
            "ID":           user[0],
            "Name":         user[1],
            "Surname":      user[2],
            "Lastname":     user[3],
            "Post":         user[4],
            "Department":   user[5],
            "Login":        user[6]
        }
        if edit_user_info["Lastname"] == None: edit_user_info["Lastname"] = "<отсутствует>"
        if edit_user_info["Department"] == None: edit_user_info["Department"] = "<отсутствует>"
        if edit_user_info["Post"] == "root": edit_user_info["Post"] = "Сис.Админ"
        elif edit_user_info["Post"] == "admin": edit_user_info["Post"] = "Администратор"
        elif edit_user_info["Post"] == "worker": edit_user_info["Post"] = "Работник"
        elif edit_user_info["Post"] == "trainee": edit_user_info["Post"] = "Стажер"

        send_user_info.append(edit_user_info)
    return(send_user_info)

def CREATE_NEW_WORKER(executor, Name, Surname, Lastname, Post, Department, Login, Password):
    connection = psycopg2.connect(
        host=config.host,
        user=config.user,
        password=config.password,
        database=config.db_name
    )

    cursor = connection.cursor()
    cursor.execute("SELECT login FROM workers where login = '"+ Login +"';")
    result = cursor.fetchall()
    if len(result) != 0:
        connection.commit()
        connection.close()
        return "User is already exist"
    connection.commit()
    sql = "INSERT INTO workers (id, name, surname,"
    values = "VALUES (DEFAULT, '" + Name + "', '" + Surname + "',"
    if Lastname != "":
        sql += "lastname,"
        values += "'" + Lastname + "',"
    if Department != "":
        sql += "department,"
        values += "'" + Department + "',"
    sql += " login, password, post)"
    values += "'" + Login + "', md5('" + Password + "'),"
    if Post == "Администратор": values += "'admin')"
    elif Post == "Работник":    values += "'worker')"
    else: values += "'trainee')"

    #print(sql + " " + values)
    cursor.execute(sql + " " + values)
    connection.commit()
    #Допилить функцию логирования
    #cursor.execute("INSERT INTO logs(initiator_id, datetime, event, end_user VALUES(" + int(executor) + ", DEFAULT, 'Создал пользователя', 2)");
    connection.close()
    return True

def GET_LOGS(id=0):
    connection = psycopg2.connect(
        host=config.host,
        user=config.user,
        password=config.password,
        database=config.db_name
    )

    cursor = connection.cursor()
    if id == 0:
        cursor.execute("SELECT * FROM logs WHERE initiator_id != '1' or end_user = '1' ")
    else:
        cursor.execute("SELECT * FROM logs WHERE initiator_id = '" + str(id) + "' or end_user = '" + str(id) + "' ")
    result = cursor.fetchall()
    connection.close()
    #return (str(result[0][1]))

    send_info = []
    for info in result:
        if info[3] == None: end_user = ""
        else: end_user = info[3]

        edit_user_info = {
            "Initiator": info[0],
            "Date": info[1].strftime("%d.%m.%Y"),
            "Time": info[1].strftime("%X"),
            "Event": info[2],
            "End_user": end_user
        }
        send_info.append(edit_user_info)
    return (send_info)

def LOAD_NEWS():
    connection = psycopg2.connect(
        host=config.host,
        user=config.user,
        password=config.password,
        database=config.db_name
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM news")
    result = cursor.fetchall()

    if not result: return None

    send_info = []
    for info in result:
        edit_info = {
            "Id": info[0],
            "Title": info[1],
            "Author": info[2],
            "Date": info[3].strftime("%d.%m.%Y"),
            "Content": info[4]
        }

        send_info.append(edit_info)
    send_info = reversed(send_info)
    return(send_info)

def DELETE_WORKER(executor, ID, name, surname):
    connection = psycopg2.connect(
        host=config.host,
        user=config.user,
        password=config.password,
        database=config.db_name
    )
    cursor = connection.cursor()
    cursor.execute("DELETE FROM workers WHERE id = '" + ID + "' and name = '" + name + "' and surname = '" + surname + "'")
    connection.commit()
    cursor.execute("SELECT id, name, surname FROM workers WHERE id = '" + ID + "'")
    result = cursor.fetchall()
    connection.close()
    if not result: return True
    else: return False

def CHANGE_WORKERDATA(executor, ID, name, surname, lastname, department, post):
    connection = psycopg2.connect(
        host=config.host,
        user=config.user,
        password=config.password,
        database=config.db_name
    )

    sql = "UPDATE workers SET name = '" + name + "', surname = '" + surname + "'"
    sqlcheck = "SELECT ID FROM workers WHERE name = '" + name + "' and surname = '" + surname + "'"

    if lastname == "<отсутствует>" or lastname == "" or lastname == " ":
        sql+= ", lastname = NULL"
    else:
        sql+= ", lastname = '" + lastname + "'"
        sqlcheck += " and lastname = '" + lastname + "'"

    if department == "<отсутствует>" or department == "" or department == " ":
        sql+= ", department = NULL"
    else:
        sql+= ", department = '" + department + "'"
        sqlcheck += " and department = '" + department + "'"



    sql += ", post = '" + post + "' WHERE id = 5"
    sqlcheck += " and post = '" + post + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    cursor.execute(sqlcheck)
    result = cursor.fetchall()
    connection.close()
    if not result: return False
    else: return True

def GET_DOCTORS(executor, ID = None):
    connection = psycopg2.connect(
            host = config.host,
            user = config.user,
            password = config.password,
            database = config.db_name
        )

    cursor = connection.cursor()
    if ID != None:
        cursor.execute("SELECT ID, name, surname, lastname, profile, workdays, workhours_start, workhours_end FROM doctors WHERE id = '" + str(ID) + "'")
    else:
        cursor.execute("SELECT ID, name, surname, lastname, profile, workdays, workhours_start, workhours_end FROM doctors")
    result = cursor.fetchall()
    connection.close()

    send_user_info=[]
    for user in result:
        workhours = str(user[6])[0:5] + " - " + str(user[7])[0:5]
        edit_user_info = {
            "ID":           user[0],
            "Name":         user[1],
            "Surname":      user[2],
            "Lastname":     user[3],
            "Profile":      user[4],
            "Workdays":     user[5],
            "Workhours":    workhours
        }
        if edit_user_info["Lastname"] == None: edit_user_info["Lastname"] = "<отсутствует>"
        send_user_info.append(edit_user_info)
    return(send_user_info)

def GET_CLIENTS(executor, ID = None):
    connection = psycopg2.connect(
            host = config.host,
            user = config.user,
            password = config.password,
            database = config.db_name
        )

    cursor = connection.cursor()
    if ID != None:
        cursor.execute("SELECT ID, name, surname, lastname, address, medical_id, phone FROM clients WHERE id = '" + str(ID) + "'")
    else:
        cursor.execute("SELECT ID, name, surname, lastname, address, medical_id, phone FROM clients")
    result = cursor.fetchall()
    connection.close()

    send_user_info=[]
    for user in result:
        edit_user_info = {
            "ID":           user[0],
            "Name":         user[1],
            "Surname":      user[2],
            "Lastname":     user[3],
            "Address":      user[4],
            "MedicalID":   user[5],
            "Phone":        user[6]
        }
        if edit_user_info["Lastname"] == None: edit_user_info["Lastname"] = "<отсутствует>"
        if edit_user_info["Phone"] == None: edit_user_info["Phone"] = "<отсутствует>"
        send_user_info.append(edit_user_info)
    return(send_user_info)

#Testing
if __name__ == "__main__":
    print(LOGIN_WORKER("root", "root"))


