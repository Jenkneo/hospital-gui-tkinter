import random

def EntryChecker(Name, Surname, Lastname, Post, Department, Login="login", Password="password"):
    # Check unique
    if Name == "":          return ("empty", "Имя")
    elif Surname == "":     return ("empty", "Фамилия")
    elif Post == "":        return ("empty", "Уровень доступа")
    elif Login == "":       return ("empty", "Логин")
    elif Password == "":    return ("empty", "Пароль")

    # check spaces
    if Name.find(" ") != -1:        return ("spaces", "Имя")
    elif Surname.find(" ") != -1:   return ("spaces", "Фамилия")
    elif Lastname.find(" ") != -1:  return ("spaces", "Отчество")
    elif Post.find(" ") != -1:      return ("spaces", "Уровень доступа")
    #elif Department.find(" ") != -1:return ("spaces", "Должность")
    elif Login.find(" ") != -1:     return ("spaces", "Логин")

    if len(Name) > 32: return ("length", "Имя")
    if len(Surname) > 32: return ("length", "Фамилия")
    if len(Lastname) > 32: return ("length", "Отчество")
    if len(Department) > 32: return ("length", "Должность")
    if len(Login) > 32: return ("length", "Логин")
    if len(Password) > 32: return ("length", "Пароль")

    return True

def Password_Generator(Password_len=12):
    Big = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    Low = 'qwertyuiopasdfghjklzxcvbnm'
    Num = '1234567890'
    Spe = '!@#_$^&amp*()'

    Pass_Symbol = list(Big + Low + Num + Spe)
    random.shuffle(Pass_Symbol)
    password = ''.join([random.choice(Pass_Symbol) for x in range(Password_len)])
    return password