from tkinter import *
from tkinter import messagebox
from server_side import *
from functions import *
from config import *
import tkinter.ttk as ttk

class LoginWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("Войдите в учетную запись")
        self.root.geometry("425x250")
        self.x = (self.root.winfo_screenwidth()) / 2 - self.root.winfo_reqwidth()
        self.y = (self.root.winfo_screenheight()) / 2 - self.root.winfo_reqheight()
        self.root.geometry("+%d+%d" % (self.x, self.y))
        # self.root.protocol("WM_DELETE_WINDOW", any_command)
        # self.root.iconbitmap("anime.ico")
        self.root.resizable(width = False, height = False)
        # self.root.config(bg = BG_COLOR)

        self.login = StringVar(self.root)
        self.password = StringVar(self.root)

        self.NameWindow = Label(self.root, text = "Войдите в учетную запись", font = label_font).place(x=80, y = 30)
        self.LoginLabel = Label(self.root, text = "Логин", font = entry_font).place(x=35, y = 100)
        self.LoginEntry = Entry(self.root, textvariable = self.login)
        self.LoginEntry.place(x=125,y=100, width = 250, height = 25)
        Label(self.root, text="Пароль", font=entry_font).place(x=35, y=150)
        self.PasswordEntry = Entry(self.root, textvariable = self.password)
        self.PasswordEntry.place(x=125,y=150, width = 250, height = 25)
        Button(self.root, text="Войти", font=entry_font, command=self.Login).place(x=190, y=200)

        self.root.bind('<Return>', self.Submit)

    def Submit(self, event): self.Login()

    def Login(self):
        if self.login.get() == "" or self.password.get() == "":
            messagebox.showinfo("Предупреждение", "Остались пустые поля")
            return None
        user = LOGIN_WORKER(self.login.get(), self.password.get())
        if user == None:
            messagebox.showinfo("Ошибка", "Возможно вы неправильно ввели логин или пароль.")
        elif user == "db_err":
            messagebox.showinfo("Ошибка", "Не удалось подключиться к базе данных.")
        elif user != None:
            messagebox.showinfo("Предупреждение!",
                                "Тут нет функционала! АБСОЛЮТНО! Исключительно пример оконного приложения которое я писал очень очень давно")
            self.root.destroy()
            MainWindow(user)

    def run(self):#
        self.root.mainloop()#

class MainWindow:
    def __init__(self, user):
        #self.User = user
        self.UserID = user["ID"]
        self.CurrentUsername = user['Name']
        self.Post = user['Post']

        self.root = Tk()
        self.root.title("Электронная регистратура")
        self.root.geometry("1250x640")
        self.root.iconbitmap("icons\logo.ico")
        self.root.resizable(width = False, height = False)
        self.root.config(bg = "#F0F1F3")


        #images
        self.image_clients =            PhotoImage(file="icons\\group.png")
        self.image_notes =              PhotoImage(file="icons\\book.png")
        self.image_statistic =          PhotoImage(file="icons\\analytic.png")
        self.image_admin_settings =     PhotoImage(file="icons\\admin.png")
        self.image_doctors =            PhotoImage(file="icons\\doctors.png")
        self.image_settings =           PhotoImage(file="icons\\settings.png")
        self.image_help =               PhotoImage(file="icons\\help.png")
        self.image_placeholder =        PhotoImage(file="icons\\placeholder.png")
        self.image_reload =             PhotoImage(file="icons\\refresh.png")
        self.image_search =             PhotoImage(file="icons\\search.png")
        self.image_user_placeholder =   PhotoImage(file="icons\\user.png")
        self.logout_user_image =        PhotoImage(file="icons\\logout.png")
        self.settings_user_image =      PhotoImage(file="icons\\wrench.png")
        self.image_edit_info =          PhotoImage(file="icons\\edit.png")
        self.win_in_win =               PhotoImage(file="icons\\win_in_win.png")
        self.plus =                     PhotoImage(file="icons\\plus.png")

        #variables
        self.worker_table_ID = StringVar()
        self.worker_table_Name = StringVar()
        self.worker_table_Surname = StringVar()
        self.worker_table_Lastname = StringVar()
        self.worker_table_Post = StringVar()
        self.worker_table_Department = StringVar()

        self.worker_table_edit_Name = StringVar()
        self.worker_table_edit_Surname = StringVar()
        self.worker_table_edit_Lastname = StringVar()
        self.worker_table_edit_Post = StringVar()
        self.worker_table_edit_Department = StringVar()

        self.btn_clients = Button(self.root, image = self.image_clients, font = button_font, relief='flat', compound="top", text = "Клиенты", command=self.open_clients)
        self.btn_notes = Button(self.root, image=self.image_notes, font=button_font, relief='flat', compound="top", text="Записи", command=self.open_notes)
        self.btn_doctors = Button(self.root, image=self.image_doctors, font=button_font, relief='flat', compound="top", text="Доктора", command=self.open_doctors)
        self.btn_admin_settings = Button(self.root, image=self.image_admin_settings, font=button_font, relief='flat', compound="top", text="Управление", command=self.open_admin_settings)
        self.btn_settings = Button(self.root, image=self.image_settings, font=button_font, relief='flat', compound="top", text="Настройки", command=self.open_settings)
        self.btn_help = Button(self.root, image=self.image_help, font=button_font, relief='flat', compound="top", text="Помощь", command=self.open_help)

        self.btn_clients.place(x =5, y=20, width=75)
        self.btn_notes.place(x=5, y=100, width=75)
        self.btn_doctors.place(x=5, y=180, width=75)
        self.btn_admin_settings.place(x=5, y=260, width=75)
        self.btn_settings.place(x=5, y=480, width=75)
        self.btn_help.place(x=5, y=560, width=75)


        self.preload_control_frames()
        self.preload_clients_frames()
        self.preload_doctors_frames(),
        self.preload_notes_frames()

        #self.load_notifications()
        self.load_current_user_info()

        self.open_clients()

        # <-------------------------- static frames ---------------------------->

    def open_clients(self):
        self.reset()
        self.image_clients = PhotoImage(file="icons\\group_selected.png")
        self.btn_clients.config(image=self.image_clients)

        self.Clients_frame.place(x=90, y=10, width=790, height=610)

    def open_settings(self):
        self.reset()
        self.image_settings = PhotoImage(file="icons\\settings_selected.png")
        self.btn_settings.config(image=self.image_settings)

    def open_help(self):
        self.reset()
        self.image_help = PhotoImage(file="icons\\help_selected.png")
        self.btn_help.config(image=self.image_help)

    def open_notes(self):
        self.reset()
        self.image_notes = PhotoImage(file="icons\\book_selected.png")
        self.btn_notes.config(image=self.image_notes)

        self.Notes_frame.place(x=90, y=10, width=790, height=610)

    def open_doctors(self):
        self.reset()
        self.image_doctors = PhotoImage(file="icons\\doctors_selected.png")
        self.btn_doctors.config(image=self.image_doctors)

        self.Doctor_frame.place(x=90, y=10, width=790, height=610)

    def open_admin_settings(self):
        self.reset()
        self.image_admin_settings = PhotoImage(file="icons\\admin_selected.png")
        self.btn_admin_settings.config(image=self.image_admin_settings)

        self.admin_settings_frame.place(x=90, y=10, width = 790, height=610)

    def preload_control_frames(self):
        self.admin_settings_frame = Frame(self.root, background="#F0F1F3")

        self.frame_worker_info_lable = Frame(self.admin_settings_frame, background="#D1E5FF")
        self.frame_worker_info_lable.place(x=0, y=0, width=290, height=40)
        self.label_worker_info = Label(self.frame_worker_info_lable, text="Информация", font=label_frame_font, background="#D1E5FF").place(x=10, y=3)


        self.create_worker = Button(self.frame_worker_info_lable, background="#D1E5FF", image = self.plus, relief='flat', command = lambda:CreateNewWorkerForm(self.root, self.UserID))
        self.create_worker.place(x=245,y=1, height=38)

        self.selected_user_frame_placeholder = Frame(self.admin_settings_frame, background="#C6D8FF")
        self.selected_user_frame_placeholder.place(x=0, y=40, width=290, height=260)
        self.placeholder1 = Label(self.selected_user_frame_placeholder, text="Создайте нового пользователя, нажав на\n", image=self.plus, compound="bottom", background="#C6D8FF").place(x=30,y=50+10)
        self.placeholder2 = Label(self.selected_user_frame_placeholder, text="Или выберите из таблицы ниже", background="#C6D8FF").place(x=55,y=150+10)


        self.selected_user_frame = Frame(self.admin_settings_frame, background="#FFF")
        self.lbl_title = ("Имя:", "Фамилия:", "Отчество:", "Доступ:", "Должность:", "Логин:", "Пароль:")
        for lbl in range(0, len(self.lbl_title)):
            self.lbl = Label(self.selected_user_frame, text=self.lbl_title[lbl], font=entry_font, background="#FFF").place(x=10, y=10 + 31 * lbl)
        for bg in range(0, len(self.lbl_title)):
            self.bg = Frame(self.selected_user_frame, background=entry_color).place(x=110, y=10 + 31 * bg, width=170, height=25)

        self.NameLabel = Label(self.selected_user_frame, font=entry_font, background=entry_color);              self.NameLabel.place(x=110, y=10)
        self.SurnameLabel = Label(self.selected_user_frame, font=entry_font, background=entry_color);           self.SurnameLabel.place(x=110, y=41)
        self.LastnameLabel = Label(self.selected_user_frame, font=entry_font, background=entry_color);          self.LastnameLabel.place(x=110, y=112 - 40)
        self.PostLabel = Label(self.selected_user_frame, font=entry_font, background=entry_color);              self.PostLabel.place(x=110, y=103)
        self.DepartmentLabel = Label(self.selected_user_frame, font=entry_font, background=entry_color);        self.DepartmentLabel.place(x=110, y=174 - 40)
        self.LoginLabel = Label(self.selected_user_frame, font=entry_font, background=entry_color);             self.LoginLabel.place(x=110, y=165)
        self.PasswordLabel = Label(self.selected_user_frame, font=entry_font, background=entry_color);          self.PasswordLabel.place(x=110, y=196)
        self.ChangeUserData = Button(self.selected_user_frame, text="Изменить", command = self.change_worker_data); self.ChangeUserData.place(x=10, y=196+31, width=130, height=25)
        self.DeleteUser = Button(self.selected_user_frame, text="Удалить пользователя", command = self.delete_worker);self.DeleteUser.place(x=151, y=196+31, width=130, height=25)

        self.selected_user_frame_changedata = Frame(self.admin_settings_frame, background="#FFF")
        for lbl in range(0, len(self.lbl_title)):
            self.lbl = Label(self.selected_user_frame_changedata, text=self.lbl_title[lbl], font=entry_font, background="#FFF").place(x=10, y=10 + 31 * lbl)
        self.NameEntry = Entry(self.selected_user_frame_changedata, background = entry_color, font=entry_font, textvariable=self.worker_table_edit_Name);              self.NameEntry.place(x=110, y=10, width=170)
        self.SurnameEntry = Entry(self.selected_user_frame_changedata, background = entry_color, font=entry_font, textvariable=self.worker_table_edit_Surname);           self.SurnameEntry.place(x=110, y=41, width=170)
        self.LastnameEntry = Entry(self.selected_user_frame_changedata, background = entry_color, font=entry_font, textvariable=self.worker_table_edit_Lastname);          self.LastnameEntry.place(x=110, y=112 - 40, width=170)
        self.PostEntry = Entry(self.selected_user_frame_changedata, background = entry_color, font=entry_font, textvariable=self.worker_table_edit_Department);              self.PostEntry.place(x=110, y=174 - 40, width=170)
        self.DepartmentEntry = ttk.Combobox(self.selected_user_frame_changedata, state="readonly", values=["Администратор", "Работник", "Стажер"], font=entry_font,textvariable=self.worker_table_edit_Post); self.DepartmentEntry.place(x=110, y=103, width=170)
        self.bg = Frame(self.selected_user_frame_changedata, background=entry_color).place(x=110, y=165, width=170, height=25)
        self.LoginEntry = Label(self.selected_user_frame_changedata, background = entry_color, font=entry_font);             self.LoginEntry.place(x=110, y=165)
        self.PasswordEntry = Button(self.selected_user_frame_changedata, background = entry_color, text = "Изменить пароль", font=entry_font, command= lambda: ChangePasswordWindow(self.root, self.UserID, self.worker_table_ID.get()));         self.PasswordEntry.place(x=110, y=196, width=170, height=25)
        self.SaveUserData = Button(self.selected_user_frame_changedata, background = entry_color, text="Сохранить", comman=self.save_workerdata); self.SaveUserData.place(x=10, y=196+31, width=130, height=25)
        self.CancelSaveUserData = Button(self.selected_user_frame_changedata, background = entry_color, text="Отмена", command = self.Cancel_save_workerdata); self.CancelSaveUserData.place(x=151, y=196+31, width=130, height=25)

        self.title_frame_worker_action = Frame(self.admin_settings_frame, background="#D1E5FF")
        self.label_worker_action = Label(self.title_frame_worker_action, text="Действия", font=label_frame_font, background="#D1E5FF").place(x=10, y=3)
        self.btn_open_in_win_worker_action = Button(self.title_frame_worker_action, image=self.win_in_win, relief='flat', background="#D1E5FF")
        self.btn_open_in_win_worker_action.place(x=445, y=1, height=38)
        self.title_frame_worker_action.place(x=300, y=0, width=490, height=40)

        self.frame_worker_action_placeholder = Frame(self.admin_settings_frame, background="#C6D8FF")
        self.frame_worker_action_placeholder.place(x=300, y=40, width=490, height=260)
        self.placeholder1 = Label(self.frame_worker_action_placeholder, text="Откройте аудит, нажав на\n", image=self.win_in_win, compound="bottom", background="#C6D8FF").place(x=165,y=50+10)
        self.placeholder2 = Label(self.frame_worker_action_placeholder, text="Или выберите конкретный аккаунт из таблицы ниже", background="#C6D8FF").place(x=85,y=150+10)

        self.frame_worker_action_table = Frame(self.admin_settings_frame, background="#888")
        self.worker_action_table = ttk.Treeview(self.frame_worker_action_table, show="headings",columns=("#1", "#2", "#3", "#4", "#5"))
        self.worker_action_table.column("#1", width=65, stretch=NO, anchor="n");      self.worker_action_table.heading("#1", text="Дата")
        self.worker_action_table.column("#2", width=55, stretch=NO, anchor="n");     self.worker_action_table.heading("#2", text="Время")
        self.worker_action_table.column("#3", width=80, stretch=NO, anchor="n");     self.worker_action_table.heading("#3", text="ID Работника")
        self.worker_action_table.column("#4", width=171, stretch=NO, anchor="n");     self.worker_action_table.heading("#4", text="Действие")
        self.worker_action_table.column("#5", width=100, stretch=NO, anchor="n");     self.worker_action_table.heading("#5", text="ID Пользователя")
        self.worker_list_action_skb = ttk.Scrollbar(self.frame_worker_action_table, orient="vertical", command=self.worker_action_table.yview)
        self.worker_action_table.configure(yscrollcommand=self.worker_list_action_skb.set)
        self.worker_action_table.place(x=0, y=0, height=260)
        self.worker_list_action_skb.place(x=473, y=0, height=260)


        self.frame_worker_list = Frame(self.admin_settings_frame, background="#888")
        self.frame_worker_list.place(x=0, y=310, width=790, height=300)
        self.title_frame_worker_list = Frame(self.frame_worker_list, background="#D1E5FF")
        self.label_worker_list = Label(self.title_frame_worker_list, text="Список работников", font=label_frame_font, background="#D1E5FF").place(x=10, y=3)

        self.btn_refresh_table = Button(self.title_frame_worker_list, image=self.image_reload, text = "Обновить", relief='flat', compound="left", background="#D1E5FF", font=button_font, command = self.refresh_worker_table)
        self.btn_refresh_table.place(x=210, y=1, height=38)
        self.entry_search_worker_list = Entry(self.title_frame_worker_list)
        self.entry_search_worker_list.place(x=540,y=5, width = 150, height = 30)

        self.btn_search_worker_list = Button(self.title_frame_worker_list, image=self.image_search, text = "Поиск", relief='flat', compound="left", background="#D1E5FF", font=button_font)
        self.btn_search_worker_list.place(x=700, y=1, height=38)
        self.title_frame_worker_list.place(x=0, y=0, width=790, height=40)

        self.worker_list_table = ttk.Treeview(self.frame_worker_list, show="headings", columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7"))
        self.worker_list_table.column("#1", width = 60, stretch=NO, anchor="n");    self.worker_list_table.heading("#1", text="ID")
        self.worker_list_table.column("#2", width = 110, stretch=NO, anchor="n");   self.worker_list_table.heading("#2", text="Имя")
        self.worker_list_table.column("#3", width = 110, stretch=NO, anchor="n");   self.worker_list_table.heading("#3", text="Фамилия")
        self.worker_list_table.column("#4", width = 120, stretch=NO, anchor="n");   self.worker_list_table.heading("#4", text="Отчество")
        self.worker_list_table.column("#5", width = 150, stretch=NO, anchor="n");   self.worker_list_table.heading("#5", text="Должность")
        self.worker_list_table.column("#6", width = 140, stretch=NO, anchor="n");   self.worker_list_table.heading("#6", text="Уровень доступа")
        self.worker_list_table.column("#7", width = 81, stretch=NO, anchor="n");    self.worker_list_table.heading("#7", text="Логин")
        self.worker_list_table_skb = ttk.Scrollbar(self.frame_worker_list, orient="vertical", command=self.worker_list_table.yview)
        self.worker_list_table.configure(yscrollcommand=self.worker_list_table_skb.set)
        self.worker_list_table.place(x=0, y=40, height=260)
        self.worker_list_table_skb.place(x=773, y=40, height=260)

        self.refresh_worker_table()

        self.worker_list_table.bind("<<TreeviewSelect>>", self.select_user_from_worker_table) #Бинд команды

    def preload_clients_frames(self):
        self.Clients_frame = Frame(self.root, background="#F0F1F3")

        self.Client_frame_info_lable = Frame(self.Clients_frame, background="#D1E5FF")
        self.Client_frame_info_lable.place(x=0, y=0, width=290, height=40)
        self.Client_label_info = Label(self.Client_frame_info_lable, text="Информация", font=label_frame_font, background="#D1E5FF").place(x=10, y=3)
        self.Client_create_btn = Button(self.Client_frame_info_lable, background="#D1E5FF", image = self.plus, relief='flat', command = lambda:CreateNewClientForm(self.root, self.UserID))
        self.Client_create_btn.place(x=245,y=1, height=38)

        self.Client_selected_frame_placeholder = Frame(self.Clients_frame, background="#C6D8FF")
        self.Client_selected_frame_placeholder.place(x=0, y=40, width=290, height=260)
        self.placeholder1 = Label(self.Client_selected_frame_placeholder, text="Создайте новую запись о клиенте, нажав на\n", image=self.plus, compound="bottom", background="#C6D8FF").place(x=20,y=50+10)
        self.placeholder2 = Label(self.Client_selected_frame_placeholder, text="Или выберите из таблицы ниже", background="#C6D8FF").place(x=55,y=150+10)

        self.selected_client_frame = Frame(self.Clients_frame, background="#FFF")
        self.lbl_title = ("ФИО:", "Улица:", "", "Телефон:", "Блок:" , "Полис ОМС:", "Паспорт" )
        for lbl in range(0, len(self.lbl_title)):
            Label(self.selected_client_frame, text=self.lbl_title[lbl], font=entry_font, background="#FFF").place(x=10, y=10 + 31 * lbl)
        for bg in range(0, len(self.lbl_title)):
            if bg == 1: Frame(self.selected_client_frame, background=entry_color).place(x=120, y=10 + 31 * bg, width=160, height=25+31)
            Frame(self.selected_client_frame, background=entry_color).place(x=120, y=10 + 31 * bg, width=160, height=25)


        self.Client_Sel_NameLabel = Label(self.selected_client_frame, font=entry_font, background=entry_color);              self.Client_Sel_NameLabel.place(x=120, y=10)
        self.Client_Sel_AddressLabel = Label(self.selected_client_frame, font=entry_font, background=entry_color);           self.Client_Sel_AddressLabel.place(x=120, y=41)
        self.Client_Sel_PhoneLabel = Label(self.selected_client_frame, font=entry_font, background=entry_color);             self.Client_Sel_PhoneLabel.place(x=120, y=103)
        self.Client_Sel_BlockLabel = Label(self.selected_client_frame, font=entry_font, background=entry_color);             self.Client_Sel_BlockLabel.place(x=120, y=134)
        self.Client_Sel_MedicalIDLabel = Label(self.selected_client_frame, font=entry_font, background=entry_color);         self.Client_Sel_MedicalIDLabel.place(x=120, y=165)
        self.Client_Sel_PassportLabel = Label(self.selected_client_frame, font=entry_font, background=entry_color);          self.Client_Sel_PassportLabel.place(x=120, y=165+31)

        self.Client_Sel_ChangeUserData = Button(self.selected_client_frame, text="Изменить"); self.Client_Sel_ChangeUserData.place(x=10, y=196+31, width=130, height=25)
        self.Client_Sel_DeleteUser = Button(self.selected_client_frame, text="Архивировать");self.Client_Sel_DeleteUser.place(x=151, y=196+31, width=130, height=25)

        self.Client_frame_action_table = Frame(self.Clients_frame, background="#888")
        self.Client_action_table = ttk.Treeview(self.Client_frame_action_table, show="headings",columns=("#1", "#2", "#3", "#4", "#5","$6", "#7"))
        self.Client_action_table.column("#1", width=30, stretch=NO, anchor="n");      self.Client_action_table.heading("#1", text="-")
        self.Client_action_table.column("#2", width=60, stretch=NO, anchor="n");     self.Client_action_table.heading("#2", text="Дата")
        self.Client_action_table.column("#3", width=50, stretch=NO, anchor="n");     self.Client_action_table.heading("#3", text="Время")
        self.Client_action_table.column("#4", width=90, stretch=NO, anchor="n");     self.Client_action_table.heading("#4", text="Тип")
        self.Client_action_table.column("#5", width=100, stretch=NO, anchor="n");     self.Client_action_table.heading("#5", text="Врач")
        self.Client_action_table.column("#6", width=100, stretch=NO, anchor="n");     self.Client_action_table.heading("#6", text="Спец")
        self.Client_action_table.column("#7", width=41, stretch=NO, anchor="n");     self.Client_action_table.heading("#7", text="Каб")
        self.Client_list_action_skb = ttk.Scrollbar(self.Client_frame_action_table, orient="vertical", command=self.Client_action_table.yview)
        self.Client_action_table.configure(yscrollcommand=self.Client_list_action_skb.set)
        self.Client_action_table.place(x=0, y=0, height=260)
        self.Client_list_action_skb.place(x=473, y=0, height=260)





        self.Client_title_frame_action = Frame(self.Clients_frame, background="#D1E5FF")
        self.Client_label_action = Label(self.Client_title_frame_action, text="Записи", font=label_frame_font, background="#D1E5FF").place(x=10, y=3)
        self.Client_btn_open_in_win_action = Button(self.Client_title_frame_action, image=self.win_in_win, relief='flat', background="#D1E5FF")
        self.Client_btn_open_in_win_action.place(x=445, y=1, height=38)
        self.Client_title_frame_action.place(x=300, y=0, width=490, height=40)

        self.Client_frame_action_placeholder = Frame(self.Clients_frame, background="#C6D8FF")
        self.Client_frame_action_placeholder.place(x=300, y=40, width=490, height=260)
        self.placeholder1 = Label(self.Client_frame_action_placeholder, text="Откройте записи, нажав на\n", image=self.win_in_win, compound="bottom", background="#C6D8FF").place(x=165,y=50+10)
        self.placeholder2 = Label(self.Client_frame_action_placeholder, text="Или выберите клиента из таблицы ниже", background="#C6D8FF").place(x=122,y=150+10)


        self.Cleint_frame_list = Frame(self.Clients_frame, background="#888")
        self.Cleint_frame_list.place(x=0, y=310, width=790, height=300)
        self.Cleint_title_frame_list = Frame(self.Cleint_frame_list, background="#D1E5FF")
        self.Cleint_title_frame_list.place(x=0, y=0, width=790, height=40)
        self.Client_label_list = Label(self.Cleint_title_frame_list, text="Список клиентов", font=label_frame_font, background="#D1E5FF").place(x=10, y=3)
        self.btn_refresh_client_table = Button(self.Cleint_title_frame_list, image=self.image_reload, text = "Обновить", relief='flat', compound="left", background="#D1E5FF", font=button_font)
        self.btn_refresh_client_table.place(x=210, y=1, height=38)
        self.entry_search_client_list = Entry(self.Cleint_title_frame_list)
        self.entry_search_client_list.place(x=540,y=5, width = 150, height = 30)
        self.btn_search_client_list = Button(self.Cleint_title_frame_list, image=self.image_search, text = "Поиск", relief='flat', compound="left", background="#D1E5FF", font=button_font)
        self.btn_search_client_list.place(x=700, y=1, height=38)

        self.client_list_table = ttk.Treeview(self.Cleint_frame_list, show="headings", columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7"))
        self.client_list_table.column("#1", width = 60, stretch=NO, anchor="n");    self.client_list_table.heading("#1", text="ID")
        self.client_list_table.column("#2", width = 110, stretch=NO, anchor="n");   self.client_list_table.heading("#2", text="Имя")
        self.client_list_table.column("#3", width = 110, stretch=NO, anchor="n");   self.client_list_table.heading("#3", text="Фамилия")
        self.client_list_table.column("#4", width = 120, stretch=NO, anchor="n");   self.client_list_table.heading("#4", text="Отчество")
        self.client_list_table.column("#5", width = 150, stretch=NO, anchor="n");   self.client_list_table.heading("#5", text="Улица")
        self.client_list_table.column("#6", width = 110, stretch=NO, anchor="n");   self.client_list_table.heading("#6", text="ОМС")
        self.client_list_table.column("#7", width = 111, stretch=NO, anchor="n");    self.client_list_table.heading("#7", text="Телефон")
        self.client_list_table_skb = ttk.Scrollbar(self.Cleint_frame_list, orient="vertical", command=self.client_list_table.yview)
        self.client_list_table.configure(yscrollcommand=self.client_list_table_skb.set)
        self.client_list_table.place(x=0, y=40, height=260)
        self.client_list_table_skb.place(x=773, y=40, height=260)
        self.refresh_clients_table()



        self.client_list_table.bind("<<TreeviewSelect>>", self.select_user_from_client_table)  # Бинд команды

    def preload_doctors_frames(self):
        self.Doctor_frame = Frame(self.root, background="#F0F1F3")

        self.Doctor_frame_info_lable = Frame(self.Doctor_frame, background="#D1E5FF")
        self.Doctor_frame_info_lable.place(x=0, y=0, width=290, height=40)
        self.Doctor_label_info = Label(self.Doctor_frame_info_lable, text="Информация", font=label_frame_font, background="#D1E5FF").place(x=10, y=3)
        self.Doctor_create_btn = Button(self.Doctor_frame_info_lable, background="#D1E5FF", image = self.plus, relief='flat')
        self.Doctor_create_btn.place(x=245,y=1, height=38)

        self.Doctor_selected_frame_placeholder = Frame(self.Doctor_frame, background="#C6D8FF")
        self.Doctor_selected_frame_placeholder.place(x=0, y=40, width=290, height=260)
        self.placeholder1 = Label(self.Doctor_selected_frame_placeholder, text="Создайте новую запись о клиенте, нажав на\n", image=self.plus, compound="bottom", background="#C6D8FF").place(x=20,y=50+10)
        self.placeholder2 = Label(self.Doctor_selected_frame_placeholder, text="Или выберите из таблицы ниже", background="#C6D8FF").place(x=55,y=150+10)

        self.selected_doctor_frame = Frame(self.Doctor_frame, background="#FFF")
        self.lbl_title = ("Имя:", "Фамилия:", "Отчество:", "Профиль:","", "Дни работы:", "Время работы:")
        for lbl in range(0, len(self.lbl_title)):
            Label(self.selected_doctor_frame, text=self.lbl_title[lbl], font=entry_font, background="#FFF").place(x=10, y=10 + 31 * lbl)
        for bg in range(0, len(self.lbl_title)):
            if bg == 3: Frame(self.selected_doctor_frame, background=entry_color).place(x=120, y=10 + 31 * bg, width=160, height=25+31)
            Frame(self.selected_doctor_frame, background=entry_color).place(x=120, y=10 + 31 * bg, width=160, height=25)


        self.Doc_Sel_NameLabel = Label(self.selected_doctor_frame, font=entry_font, background=entry_color);              self.Doc_Sel_NameLabel.place(x=120, y=10)
        self.Doc_Sel_SurnameLabel = Label(self.selected_doctor_frame, font=entry_font, background=entry_color);           self.Doc_Sel_SurnameLabel.place(x=120, y=41)
        self.Doc_Sel_LastnameLabel = Label(self.selected_doctor_frame, font=entry_font, background=entry_color);          self.Doc_Sel_LastnameLabel.place(x=120, y=112 - 40)
        self.Doc_Sel_ProfileLabel = Label(self.selected_doctor_frame, font=entry_font, background=entry_color);           self.Doc_Sel_ProfileLabel.place(x=120, y=103)
        self.Doc_Sel_WorkdaysLabel = Label(self.selected_doctor_frame, font=entry_font, background=entry_color);          self.Doc_Sel_WorkdaysLabel.place(x=120, y=165)
        self.Doc_Sel_WorktimeLabel = Label(self.selected_doctor_frame, font=entry_font, background=entry_color);          self.Doc_Sel_WorktimeLabel.place(x=120, y=165+31)
        # self.Doc_Sel_PasswordLabel = Label(self.selected_doctor_frame, font=entry_font, background=entry_color);          self.Doc_Sel_PasswordLabel.place(x=110, y=196)
        # self.Doc_Sel_ChangeUserData = Button(self.selected_doctor_frame, text="Изменить", command = self.change_worker_data); self.Doc_Sel_ChangeUserData.place(x=10, y=196+31, width=130, height=25)
        # self.Doc_Sel_DeleteUser = Button(self.selected_doctor_frame, text="Удалить пользователя", command = self.delete_worker);self.Doc_Sel_DeleteUser.place(x=151, y=196+31, width=130, height=25)


        self.Doctor_title_frame_action = Frame(self.Doctor_frame, background="#D1E5FF")
        self.Doctor_label_action = Label(self.Doctor_title_frame_action, text="Записи", font=label_frame_font, background="#D1E5FF").place(x=10, y=3)
        self.Doctor_btn_open_in_win_action = Button(self.Doctor_title_frame_action, image=self.win_in_win, relief='flat', background="#D1E5FF")
        self.Doctor_btn_open_in_win_action.place(x=445, y=1, height=38)
        self.Doctor_title_frame_action.place(x=300, y=0, width=490, height=40)

        self.Doctor_frame_action_placeholder = Frame(self.Doctor_frame, background="#C6D8FF")
        self.Doctor_frame_action_placeholder.place(x=300, y=40, width=490, height=260)
        self.placeholder1 = Label(self.Doctor_frame_action_placeholder, text="Откройте записи, нажав на\n", image=self.win_in_win, compound="bottom", background="#C6D8FF").place(x=165,y=50+10)
        self.placeholder2 = Label(self.Doctor_frame_action_placeholder, text="Или выберите клиента из таблицы ниже", background="#C6D8FF").place(x=122,y=150+10)


        self.Doctor_frame_list = Frame(self.Doctor_frame, background="#888")
        self.Doctor_frame_list.place(x=0, y=310, width=790, height=300)
        self.Doctor_title_frame_list = Frame(self.Doctor_frame_list, background="#D1E5FF")
        self.Doctor_title_frame_list.place(x=0, y=0, width=790, height=40)
        self.Doctor_label_list = Label(self.Doctor_title_frame_list, text="Список докторов", font=label_frame_font, background="#D1E5FF").place(x=10, y=3)
        self.btn_refresh_doctor_table = Button(self.Doctor_title_frame_list, image=self.image_reload, text = "Обновить", relief='flat', compound="left", background="#D1E5FF", font=button_font)
        self.btn_refresh_doctor_table.place(x=210, y=1, height=38)
        self.entry_search_doctor_list = Entry(self.Doctor_title_frame_list)
        self.entry_search_doctor_list.place(x=540,y=5, width = 150, height = 30)
        self.btn_search_doctor_list = Button(self.Doctor_title_frame_list, image=self.image_search, text = "Поиск", relief='flat', compound="left", background="#D1E5FF", font=button_font)
        self.btn_search_doctor_list.place(x=700, y=1, height=38)

        self.doctor_list_table = ttk.Treeview(self.Doctor_frame_list, show="headings", columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7"))
        self.doctor_list_table.column("#1", width = 60, stretch=NO, anchor="n");    self.doctor_list_table.heading("#1", text="ID")
        self.doctor_list_table.column("#2", width = 110, stretch=NO, anchor="n");   self.doctor_list_table.heading("#2", text="Имя")
        self.doctor_list_table.column("#3", width = 110, stretch=NO, anchor="n");   self.doctor_list_table.heading("#3", text="Фамилия")
        self.doctor_list_table.column("#4", width = 120, stretch=NO, anchor="n");   self.doctor_list_table.heading("#4", text="Отчество")
        self.doctor_list_table.column("#5", width = 150, stretch=NO, anchor="n");   self.doctor_list_table.heading("#5", text="Специальность")
        self.doctor_list_table.column("#6", width = 120, stretch=NO, anchor="n");   self.doctor_list_table.heading("#6", text="Дни работы")
        self.doctor_list_table.column("#7", width = 101, stretch=NO, anchor="n");    self.doctor_list_table.heading("#7", text="Время работы")
        self.doctor_list_table_skb = ttk.Scrollbar(self.Doctor_frame_list, orient="vertical", command=self.doctor_list_table.yview)
        self.doctor_list_table.configure(yscrollcommand=self.doctor_list_table_skb.set)
        self.doctor_list_table.place(x=0, y=40, height=260)
        self.doctor_list_table_skb.place(x=773, y=40, height=260)


        self.refresh_doctor_table()

        self.doctor_list_table.bind("<<TreeviewSelect>>", self.select_user_from_doctor_table)  # Бинд команды

    def preload_notes_frames(self):
        self.Notes_frame = Frame(self.root, background="#F0F1F3")

        self.Note_settings_frame_lable = Frame(self.Notes_frame, background="#D1E5FF")
        self.Note_settings_frame_lable.place(x=0, y=0, width=290, height=40)
        self.Note_settings_lable = Label(self.Note_settings_frame_lable, text="Запись", font=label_frame_font, background="#D1E5FF").place(x=10, y=3)

        self.Note_settings_paceholder_frame = Frame(self.Notes_frame, background="#C6D8FF")
        self.Note_settings_paceholder_frame.place(x=0, y=40, width=290, height=260)
        self.placeholder1 = Label(self.Note_settings_paceholder_frame, text="Создайте новую запись, нажав на\n", image=self.plus, compound="bottom", background="#C6D8FF").place(x=45,y=50+10)
        self.placeholder2 = Label(self.Note_settings_paceholder_frame, text="в таблице справа", background="#C6D8FF").place(x=90,y=135)
        self.placeholder3 = Label(self.Note_settings_paceholder_frame, text="Или выберите уже существующую запись", background="#C6D8FF").place(x=25,y=160)

        self.Notes_list_title_frame = Frame(self.Notes_frame, background="#D1E5FF")
        self.Notes_list_title = Label(self.Notes_list_title_frame, text="Список записей", font=label_frame_font, background="#D1E5FF").place(x=10, y=3)
        self.Notes_create_btn = Button(self.Notes_list_title_frame, image=self.plus, relief='flat', background="#D1E5FF")
        self.Notes_create_btn.place(x=445, y=1, height=38)
        self.Notes_list_title_frame.place(x=300, y=0, width=490, height=40)

        self.Notes_list_placeholder_frame = Frame(self.Notes_frame, background="#C6D8FF")
        self.Notes_list_placeholder_frame.place(x=300, y=40, width=490, height=260)
        self.placeholder1 = Label(self.Notes_list_placeholder_frame, text="Выберите врача и клиента\n\nиз таблиц ниже", background="#C6D8FF").place(x=165,y=90)

        self.Notes_Clients_list_frame = Frame(self.Notes_frame, background="#888")
        self.Notes_Clients_list_frame.place(x=0, y=310, width=460, height=300)
        self.Notes_Clients_list_title_frame = Frame(self.Notes_Clients_list_frame, background="#D1E5FF")
        self.Notes_Clients_list_title = Label(self.Notes_Clients_list_title_frame, text="Клиенты", font=label_frame_font, background="#D1E5FF").place(x=10, y=3)
        self.Notes_Clients_list_title_frame.place(x=0, y=0, width=460, height=40)

        self.Notes_Clients_list_entry_search = Entry(self.Notes_Clients_list_title_frame)
        self.Notes_Clients_list_entry_search.place(x=225,y=5, width = 150, height = 30)

        self.Notes_Clients_list_search_btn = Button(self.Notes_Clients_list_title_frame, image=self.image_search, text = "Поиск", relief='flat', compound="left", background="#D1E5FF", font=button_font)
        self.Notes_Clients_list_search_btn.place(x=380, y=1, height=38)

        self.Notes_Clients_table = ttk.Treeview(self.Notes_Clients_list_frame, show="headings", columns=("#1", "#2", "#3", "#4"))
        self.Notes_Clients_table.column("#1", width = 70, stretch=NO, anchor="n");    self.Notes_Clients_table.heading("#1", text="ID")
        self.Notes_Clients_table.column("#2", width = 125, stretch=NO, anchor="n");   self.Notes_Clients_table.heading("#2", text="Имя")
        self.Notes_Clients_table.column("#3", width = 126, stretch=NO, anchor="n");   self.Notes_Clients_table.heading("#3", text="Фамилия")
        self.Notes_Clients_table.column("#4", width = 120, stretch=NO, anchor="n");   self.Notes_Clients_table.heading("#4", text="ОМС")
        self.Notes_Clients_table_skb = ttk.Scrollbar(self.Notes_Clients_list_frame, orient="vertical", command=self.Notes_Clients_table.yview)
        self.Notes_Clients_table.configure(yscrollcommand=self.Notes_Clients_table_skb.set)
        self.Notes_Clients_table.place(x=0, y=40, height=260)
        self.Notes_Clients_table_skb.place(x=443, y=40, height=260)

        self.Notes_Doctors_list_frame = Frame(self.Notes_frame, background="#888")
        self.Notes_Doctors_list_frame.place(x=470, y=310, width=320, height=300)

        self.Notes_Doctors_list_title_frame = Frame(self.Notes_Doctors_list_frame, background="#D1E5FF")
        self.Notes_Doctors_list_title = Label(self.Notes_Doctors_list_title_frame, text="Доктора", font=label_frame_font, background="#D1E5FF").place(x=10, y=3)
        self.Notes_Doctors_list_title_frame.place(x=0, y=0, width=320, height=40)


        self.Notes_Doctors_list_entry_search = Entry(self.Notes_Doctors_list_title_frame)
        self.Notes_Doctors_list_entry_search.place(x=125,y=5, width = 150, height = 30)

        self.Notes_Doctors_list_search_btn = Button(self.Notes_Doctors_list_title_frame, image=self.image_search, relief='flat', background="#D1E5FF", font=button_font)
        self.Notes_Doctors_list_search_btn.place(x=280, y=1, height=38)

        self.Notes_Doctors_table = ttk.Treeview(self.Notes_Doctors_list_frame, show="headings", columns=("#1", "#2", "#3"))
        self.Notes_Doctors_table.column("#1", width = 100, stretch=NO, anchor="n");    self.Notes_Doctors_table.heading("#1", text="Имя")
        self.Notes_Doctors_table.column("#2", width = 100, stretch=NO, anchor="n");   self.Notes_Doctors_table.heading("#2", text="Фамилия")
        self.Notes_Doctors_table.column("#3", width = 101, stretch=NO, anchor="n");   self.Notes_Doctors_table.heading("#3", text="Специальность")
        self.Notes_Doctors_table_skb = ttk.Scrollbar(self.Notes_Doctors_list_frame, orient="vertical", command=self.Notes_Doctors_table.yview)
        self.Notes_Doctors_table.configure(yscrollcommand=self.Notes_Doctors_table_skb.set)
        self.Notes_Doctors_table.place(x=0, y=40, height=260)
        self.Notes_Doctors_table_skb.place(x=303, y=40, height=260)

        #<-------------------------------- Admin settings end ---------------------------------->

    def load_current_user_info(self):
        # <-------------------------- Current user & notifications start ---------------------------->
        self.frame_current_user = Frame(self.root, background="#D1E5FF")
        self.user_photo_placeholder = Label(self.frame_current_user, image=self.image_user_placeholder, background="#D1E5FF").place(x=10,y=11)
        self.name_label = Label(self.frame_current_user, text=self.CurrentUsername, fg="#000", background="#D1E5FF",  font=("Arial", 24, "bold")).place(x=55, y=10)
        self.settings_current_user = Button(self.frame_current_user, image=self.settings_user_image, relief='flat', background="#D1E5FF")
        self.logout = Button(self.frame_current_user, image=self.logout_user_image, relief='flat', background="#D1E5FF")
        self.settings_current_user.place(x=285, y=10)
        self.logout.place(x=285,y=135)

        self.img = Label(self.frame_current_user, image=self.image_placeholder, background="#D1E5FF").place(x=17, y=60)
        self.img = Label(self.frame_current_user, image=self.image_placeholder, background="#D1E5FF").place(x=17, y=94)
        self.img = Label(self.frame_current_user, image=self.image_placeholder, background="#D1E5FF").place(x=17, y=128)
        self.img = Label(self.frame_current_user, image=self.image_placeholder, background="#D1E5FF").place(x=17, y=162)

        self.current_user_post = Label(self.frame_current_user, text="Должность: Оператор", background="#D1E5FF", font=cur_user_font).place(x=46, y=61)
        self.current_user_post = Label(self.frame_current_user, text="Уровень: Работник", background="#D1E5FF", font=cur_user_font).place(x=46, y=95)
        self.current_user_post = Label(self.frame_current_user, text="Уведомления: None", background="#D1E5FF", font=cur_user_font).place(x=46, y=129)
        self.current_user_post = Label(self.frame_current_user, text="Заявок: None", background="#D1E5FF", font=cur_user_font).place(x=46, y=163)

        self.frame_current_user.place(x=890, y=10, width=350, height=200)
        # <-------------------------- Current user & notifications end ---------------------------->

    def load_notifications(self):
        self.Loaded_News = LOAD_NEWS()
        if self.Loaded_News == None:
            self.frame_notification_placeholder = Frame(self.root, background=pastel_color)
            self.frame_notification_placeholder_title = Label(self.frame_notification_placeholder, text = "Оповещения", background=pastel_color, font = ("Calibri", 20)).place(x=100+5,y=5)
            self.frame_notification_noneinfo = Label(self.frame_notification_placeholder, text = "За прошедший месяц\nоповещений нет.", background=pastel_color, font=entry_font).place(x=100+5,y=170)
            self.News_btn_open = Button(self.frame_notification_placeholder, image=self.win_in_win, relief='flat', background="#D1E5FF")
            self.News_btn_open.place(x=306, y=1, height=38)
            self.frame_notification_placeholder.place(x=890, y=220, width=350, height=400)
        else:
            self.frame_notification = Frame(self.root, background="#D1E5FF")
            self.frame_notification_title = Label(self.frame_notification, text = "Оповещения", background="#D1E5FF", font = label_frame_font).place(x=5,y=5)
            self.News_btn_open = Button(self.frame_notification, image=self.win_in_win, relief='flat', background="#D1E5FF")
            self.News_btn_open.place(x=306, y=1, height=38)

            self.place = 38
            self.i = 0
            for news in self.Loaded_News:
                self.News_Frame = Frame(self.frame_notification, background="#FFF", highlightbackground="#D1E5FF", highlightthickness=5)
                self.News_Title = Label(self.News_Frame, text = news["Title"], font = ("Calibri", 18), background="#FFF").place(x=5,y=4)
                self.News_Author = Label(self.News_Frame, text = "Автор: " + str(news["Author"]), font = ("Calibri", 10), background="#FFF").place(x=110,y=37)
                self.News_Date = Label(self.News_Frame, text = "Дата: " + news["Date"], font = ("Calibri", 10), background="#FFF").place(x=6,y=37)
                self.News_Content = Label(self.News_Frame, text = news["Content"][0:40]+"...", font = ("Calibri", 12), background="#FFF").place(x=6,y=57)
                self.News_Frame.place(x=0, y=self.place, height=94, width=350)

                self.i+=1
                if self.i == 4: break
                self.place += 89

            self.frame_notification.place(x=890, y=220, width=350, height=400)

    def Cancel_save_workerdata(self):
        self.selected_user_frame_changedata.place_forget()
        self.selected_user_frame.place(x=0, y=40, width=290, height=260)

    def change_worker_data(self):
        if str(self.UserID) == str(self.worker_table_ID.get()) and self.UserID != 1:
            messagebox.showerror("Ошибка", "Вы не можете самостоятельно редактировать свой аккаунт.\nДля редактирования своего аккаунта, обратитесь к администратору.")
            return None
        self.userinfo = GET_WORKERS(self.UserID, self.worker_table_ID.get())
        self.worker_table_edit_Name.set(self.userinfo[0]["Name"])
        self.worker_table_edit_Surname.set(self.userinfo[0]["Surname"])
        self.worker_table_edit_Lastname.set(self.userinfo[0]["Lastname"])
        self.worker_table_edit_Post.set(self.userinfo[0]["Post"])
        self.worker_table_edit_Department.set(self.userinfo[0]["Department"])
        self.selected_user_frame.place_forget()
        self.selected_user_frame_changedata.place(x=0, y=40, width=290, height=260)

    def save_workerdata(self):
        err = EntryChecker(
            self.worker_table_edit_Name.get(),
            self.worker_table_edit_Surname.get(),
            self.worker_table_edit_Lastname.get(),
            self.worker_table_edit_Post.get(),
            self.worker_table_edit_Department.get()
        )
        if err == True:
            if self.worker_table_edit_Post.get() == "Администратор": self.worker_table_edit_post_send = "admin"
            elif self.worker_table_edit_Post.get() == "Работник": self.worker_table_edit_post_send = "worker"
            elif self.worker_table_edit_Post.get() == "Стажер": self.worker_table_edit_post_send = "trainee"
            self.Feedback = CHANGE_WORKERDATA(
                self.UserID,
                self.worker_table_ID.get(),
                self.worker_table_edit_Name.get(),
                self.worker_table_edit_Surname.get(),
                self.worker_table_edit_Lastname.get(),
                self.worker_table_edit_Department.get(),
                self.worker_table_edit_post_send
            )
            if self.Feedback:
                messagebox.showinfo("Успех", "Анкета успешно обновлена!")
                self.refresh_worker_table()
            else:
                messagebox.showerror("Ошибка", "Обноновить данные не удалось.")
        elif err[0] == "empty": messagebox.showerror("Ошибка", "Поле \""+ err[1] +"\" не может быть пустым!"); return False
        elif err[0] == "spaces": messagebox.showerror("Ошибка", "В поле \"" + err[1] + "\" не могут находиться пробелы!"); return False
        elif err[0] == "length": messagebox.showerror("Ошибка", "Поле \"" + err[1] + "\" не может содержать более 32 символов!"); return False

    def delete_worker(self):
        if str(self.UserID) == str(self.worker_table_ID.get()):
            messagebox.showerror("Ошибка", "Вы не можете удалить свой аккаунт.\nДля удаления своего аккаунта, обратитесь к администратору.")
            return None

        if messagebox.askyesno("Подтвердите действие", "Вы действительно хотите удалить пользователя " + self.worker_table_Name.get() + "?"):
            if DELETE_WORKER(self.UserID, self.worker_table_ID.get(), self.worker_table_Name.get(), self.worker_table_Surname.get()):
                self.refresh_worker_table()
                messagebox.showinfo("Успех", "Пользователь успешно удален!")
                self.selected_user_frame_changedata.place_forget()
                self.selected_user_frame.place_forget()
                self.frame_worker_action_table.place_forget()
                self.selected_user_frame_placeholder.place(x=0, y=40, width=290, height=260)
                self.frame_worker_action_placeholder.place(x=300, y=40, width=490, height=260)
            else:
                messagebox.showerror("Ошибка", "Пользователя удалить не удалось.")

    def select_user_from_worker_table(self, event):
        self.selected_user_data = None
        self.selected_user_frame_changedata.place_forget()
        self.selected_user_frame_placeholder.place_forget()
        self.frame_worker_action_placeholder.place_forget()
        self.frame_worker_action_table.place(x=300, y=40, width=490, height=260)
        self.selected_user_frame.place(x=0, y=40, width=290, height=260)
        for selection in self.worker_list_table.selection():
            item = self.worker_list_table.item(selection)
            self.worker_table_ID.set(item["values"][0])
            self.worker_table_Name.set(item["values"][1])
            self.worker_table_Surname.set(item["values"][2])
            self.worker_table_Lastname.set(item["values"][3])
            self.worker_table_Post.set(item["values"][4])
            self.worker_table_Department.set(item["values"][5])

            self.NameLabel.config(text=item["values"][1])
            self.SurnameLabel.config(text=item["values"][2])
            self.LastnameLabel.config(text=item["values"][3])
            self.PostLabel.config(text=item["values"][5])
            self.DepartmentLabel.config(text=item["values"][4])
            self.LoginLabel.config(text=item["values"][6])
            self.LoginEntry.config(text=item["values"][6])
            self.PasswordLabel.config(text="********")
            last_name, first_name, email = item["values"][0:3]
            self.logs = GET_LOGS(item["values"][0])

        self.worker_action_table.delete(*self.worker_action_table.get_children())
        for pars_user in self.logs:
            self.worker_action_table.insert("", END, values=(
              pars_user["Date"],
              pars_user["Time"],
              pars_user["Initiator"],
              pars_user["Event"],
              pars_user["End_user"]
            )
                                            )

    def select_user_from_doctor_table(self, event):
        self.selected_doctor_data = None
        # self.selected_doctor_frame_changedata.place_forget()
        self.Doctor_selected_frame_placeholder.place_forget()
        self.Doctor_frame_action_placeholder.place_forget()
        # self.frame_worker_action_table.place(x=300, y=40, width=490, height=260)
        self.selected_doctor_frame.place(x=0, y=40, width=290, height=260)
        for selection in self.doctor_list_table.selection():
            item = self.doctor_list_table.item(selection)
            # self.worker_table_ID.set(item["values"][0])
            # self.worker_table_Name.set(item["values"][1])
            # self.worker_table_Surname.set(item["values"][2])
            # self.worker_table_Lastname.set(item["values"][3])
            # self.worker_table_Post.set(item["values"][4])
            # self.worker_table_Department.set(item["values"][5])

            self.Doc_Sel_NameLabel.config(text=item["values"][1])
            self.Doc_Sel_SurnameLabel.config(text=item["values"][2])
            self.Doc_Sel_LastnameLabel.config(text=item["values"][3])
            self.Doc_Sel_ProfileLabel.config(text=item["values"][4])
            self.Doc_Sel_WorkdaysLabel.config(text=item["values"][5])
            self.Doc_Sel_WorktimeLabel.config(text=item["values"][6])
            # self.Doc_Sel_LoginEntry.config(text=item["values"][6])
            # self.Doc_Sel_PasswordLabel.config(text="********")
            # last_name, first_name, email = item["values"][0:3]
            # self.logs = GET_LOGS(item["values"][0])

        # self.worker_action_table.delete(*self.worker_action_table.get_children())
        # for pars_user in self.logs:
        #     self.worker_action_table.insert("", END, values=(
        #       pars_user["Date"],
        #       pars_user["Time"],
        #       pars_user["Initiator"],
        #       pars_user["Event"],
        #       pars_user["End_user"]
        #     )
        #                                     )

    def select_user_from_client_table(self, event):
        self.selected_client_data = None
        self.Client_selected_frame_placeholder.place_forget()
        self.Client_frame_action_placeholder.place_forget()
        self.Client_frame_action_table.place(x=300, y=40, width=490, height=260)
        self.selected_client_frame.place(x=0, y=40, width=290, height=260)
        for selection in self.client_list_table.selection():
            item = self.client_list_table.item(selection)
            # self.client_table_ID.set(item["values"][0])
            # self.client_table_Name.set(item["values"][1])
            # self.client_table_Surname.set(item["values"][2])
            # self.client_table_Lastname.set(item["values"][3])
            # self.client_table_Post.set(item["values"][4])
            # self.client_table_Department.set(item["values"][5])

            self.Client_Sel_NameLabel.config(text=item["values"][2] + " " + item["values"][1][0] + "." + item["values"][3][0]+".")
            self.Client_Sel_AddressLabel.config(text=item["values"][4])
            # self.Client_Sel_PhoneLabel.config(text=item["values"][6])
            # self.Client_Sel_BlockLabel.config(text=item["values"][4])
            # self.Client_Sel_MedicalIDLabel.config(text=item["values"][5])
            # self.Client_Sel_PassportLabel.config(text=item["values"][6])
            last_name, first_name, email = item["values"][0:3]
            self.logs = GET_LOGS(item["values"][0])

        # self.worker_action_table.delete(*self.worker_action_table.get_children())
        # for pars_user in self.logs:
        #     self.worker_action_table.insert("", END, values=(
        #       pars_user["Date"],
        #       pars_user["Time"],
        #       pars_user["Initiator"],
        #       pars_user["Event"],
        #       pars_user["End_user"]
        #     )
        #                                     )

    def refresh_worker_table(self):
        self.worker_list_table.delete(*self.worker_list_table.get_children())
        self.userlist = GET_WORKERS(self.UserID)
        for pars_user in self.userlist:
            if len(pars_user["Name"]) > 17: pars_user["Name"] = pars_user["Name"][0:17] + "..."
            if len(pars_user["Surname"]) > 17: pars_user["Surname"] = pars_user["Surname"][0:17] + "..."
            if len(pars_user["Lastname"]) > 17: pars_user["Lastname"] = pars_user["Lastname"][0:17] + "..."
            if len(pars_user["Department"]) > 17: pars_user["Department"] = pars_user["Department"][0:17] + "..."
            if len(pars_user["Login"]) > 17: pars_user["Login"] = pars_user["Login"][0:17] + "..."
            self.worker_list_table.insert("", END, values=(
                pars_user["ID"],
                pars_user["Name"],
                pars_user["Surname"],
                pars_user["Lastname"],
                pars_user["Department"],
                pars_user["Post"],
                pars_user["Login"])
                                          )

    def refresh_doctor_table(self):
        self.doctor_list_table.delete(*self.doctor_list_table.get_children())
        self.doctor_list = GET_DOCTORS(self.UserID)
        for pars_user in self.doctor_list:
            if len(pars_user["Name"]) > 17: pars_user["Name"] = pars_user["Name"][0:17] + "..."
            if len(pars_user["Surname"]) > 17: pars_user["Surname"] = pars_user["Surname"][0:17] + "..."
            if len(pars_user["Lastname"]) > 17: pars_user["Lastname"] = pars_user["Lastname"][0:17] + "..."
            if len(pars_user["Profile"]) > 17: pars_user["Profile"] = pars_user["Profile"][0:17] + "..."
            self.doctor_list_table.insert("", END, values=(
                pars_user["ID"],
                pars_user["Name"],
                pars_user["Surname"],
                pars_user["Lastname"],
                pars_user["Profile"],
                pars_user["Workdays"],
                pars_user["Workhours"])
                                          )

    def refresh_clients_table(self):
        self.client_list_table.delete(*self.client_list_table.get_children())
        self.client_list = GET_CLIENTS(self.UserID)
        for pars_user in self.client_list:
            if len(pars_user["Name"]) > 17: pars_user["Name"] = pars_user["Name"][0:17] + "..."
            if len(pars_user["Surname"]) > 17: pars_user["Surname"] = pars_user["Surname"][0:17] + "..."
            if len(pars_user["Lastname"]) > 17: pars_user["Lastname"] = pars_user["Lastname"][0:17] + "..."
            if len(pars_user["Address"]) > 17: pars_user["Address"] = pars_user["Address"][0:17] + "..."
            self.client_list_table.insert("", END, values=(
                pars_user["ID"],
                pars_user["Name"],
                pars_user["Surname"],
                pars_user["Lastname"],
                pars_user["Address"],
                pars_user["MedicalID"],
                pars_user["Phone"])
                                          )

    def run(self):
        self.root.mainloop()

    def reset(self):
        self.image_clients = PhotoImage(file="icons\\group.png")
        self.image_notes = PhotoImage(file="icons\\book.png")
        self.image_doctors = PhotoImage(file="icons\\doctors.png")
        self.image_admin_settings = PhotoImage(file="icons\\admin.png")
        self.image_settings = PhotoImage(file="icons\\settings.png")
        self.image_help = PhotoImage(file="icons\\help.png")

        self.btn_clients.config(image=self.image_clients)
        self.btn_notes.config(image=self.image_notes)
        self.btn_doctors.config(image=self.image_doctors)
        self.btn_admin_settings.config(image=self.image_admin_settings)
        self.btn_settings.config(image=self.image_settings)
        self.btn_help.config(image=self.image_help)

        self.admin_settings_frame.place_forget()
        self.Clients_frame.place_forget()
        self.Notes_frame.place_forget()
        self.Doctor_frame.place_forget()

class CreateNewClientForm:
    def __init__(self, parentWindow, UserID):
        self.UserID = UserID
        self.root = Toplevel(parentWindow)
        self.root.title("[НЕ РАБОТАЕТ]Создание новой анкеты клиента")
        self.root.geometry("320x275")

        # self.root.iconbitmap("anime.ico")
        self.root.resizable(width = False, height = False)
        #self.root.wm_attributes("-topmost", 1)
        self.root.config(bg = "#FFF")


        #variables
        self.Name = StringVar()
        self.Surname = StringVar()
        self.Lastname = StringVar()
        self.Phone = StringVar()
        self.Address = StringVar()
        self.Block = StringVar()
        self.MedicalID = StringVar()
        self.Passport = StringVar()

        self.lbl_title = ("Имя:", "Фамилия:", "Отчество:", "Адрес:", "Блок:", "Полис ОМС:", "Паспорт:")
        for lbl in range(0,len(self.lbl_title)):
            self.lbl = Label(self.root, text=self.lbl_title[lbl], font=entry_font, background="#FFF").place(x=10, y = 10+31*lbl)

        self.NameEntry = Entry(self.root, font=entry_font, textvariable = self.Name, background=entry_color).place(x=110, y = 50-40, width = 200)
        self.SurnameEntry = Entry(self.root, font=entry_font, textvariable = self.Surname, background=entry_color).place(x=110, y = 81-40, width = 200)
        self.LastnameEntry = Entry(self.root, font=entry_font, textvariable = self.Lastname, background=entry_color).place(x=110, y = 112-40, width = 200)
        self.AddressEntry = Entry(self.root, font=entry_font, textvariable = self.Address, background=entry_color).place(x=110, y = 143-40, width = 200)
        self.BlockEntry = ttk.Combobox(self.root, state="readonly", values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"], font=entry_font, textvariable = self.Block, background=entry_color).place(x=110, y = 174-40, width = 200)
        self.MedicalIDEntry = Entry(self.root, font=entry_font, textvariable = self.MedicalID, background=entry_color).place(x=110, y = 205-40, width = 200)
        self.PassportEntry = Entry(self.root, font=entry_font, textvariable = self.Passport, background=entry_color).place(x=110, y = 236-40, width = 200)
        #
        # self.GenPassword = Button(self.root, text = "Ген.", command = lambda:self.Password.set(Password_Generator())).place(x=285, y=196, width=25, height=22)
        # self.ButtonSubmit = Button(self.root, text = "Создать", font=entry_font, command = self.edit_info).place(x=70, y=230)
        # self.ButtonCancel = Button(self.root, text = "Отмена", font=entry_font, command = lambda:self.root.destroy()).place(x=170, y=230)
        #
        # self.grab_focus()

class CreateNewWorkerForm: #Создание новой анкеты клиента
    def __init__(self, parentWindow, UserID):
        self.UserID = UserID
        self.root = Toplevel(parentWindow)
        self.root.title("Создание работника")
        self.root.geometry("320x275")

        # self.root.iconbitmap("anime.ico")
        self.root.resizable(width = False, height = False)
        #self.root.wm_attributes("-topmost", 1)
        self.root.config(bg = "#FFF")


        #variables
        self.Name = StringVar()
        self.Surname = StringVar()
        self.Lastname = StringVar()
        self.Post = StringVar()
        self.Department = StringVar()
        self.Login = StringVar()
        self.Password = StringVar()

        self.lbl_title = ("Имя:", "Фамилия:", "Отчество:",  "Доступ:", "Должность:", "Логин:", "Пароль:")
        for lbl in range(0,len(self.lbl_title)):
            self.lbl = Label(self.root, text=self.lbl_title[lbl], font=entry_font, background="#FFF").place(x=10, y = 10+31*lbl)

        self.NameEntry = Entry(self.root, font=entry_font, textvariable = self.Name, background=entry_color).place(x=110, y = 50-40, width = 200)
        self.SurnameEntry = Entry(self.root, font=entry_font, textvariable = self.Surname, background=entry_color).place(x=110, y = 81-40, width = 200)
        self.LastnameEntry = Entry(self.root, font=entry_font, textvariable = self.Lastname, background=entry_color).place(x=110, y = 112-40, width = 200)
        self.PostEntry = ttk.Combobox(self.root, state="readonly", values=["Администратор", "Работник", "Стажер"], font=entry_font, textvariable = self.Post).place(x=110, y = 143-40, width = 200)
        self.DepartmentEntry = Entry(self.root, font=entry_font, textvariable = self.Department, background=entry_color).place(x=110, y = 174-40, width = 200)
        self.LoginEntry = Entry(self.root, font=entry_font, textvariable = self.Login, background=entry_color).place(x=110, y = 205-40, width = 200)
        self.PasswordEntry = Entry(self.root, font=entry_font, textvariable = self.Password, background=entry_color).place(x=110, y = 236-40, width = 170)

        self.GenPassword = Button(self.root, text = "Ген.", command = lambda:self.Password.set(Password_Generator())).place(x=285, y=196, width=25, height=22)
        self.ButtonSubmit = Button(self.root, text = "Создать", font=entry_font, command = self.edit_info).place(x=70, y=230)
        self.ButtonCancel = Button(self.root, text = "Отмена", font=entry_font, command = lambda:self.root.destroy()).place(x=170, y=230)

        self.grab_focus()

    def grab_focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()

    def edit_info(self):
        err = EntryChecker(
            self.Name.get(),
            self.Surname.get(),
            self.Lastname.get(),
            self.Post.get(),
            self.Department.get(),
            self.Login.get(),
            self.Password.get()
        )
        if err == True:
            #Добавть проверку на кол-во символов и сами символы
            self.Feedback = CREATE_NEW_WORKER(
                self.UserID,
                self.Name.get(),
                self.Surname.get(),
                self.Lastname.get(),
                self.Post.get(),
                self.Department.get(),
                self.Login.get(),
                self.Password.get()
                )
            if self.Feedback == True:
                messagebox.showinfo("Успех", "Анкета успешно создана!\nЧтобы пользователь отобразился, обновите таблицу.")
                self.root.destroy()
            elif self.Feedback == "User is already exist":
                messagebox.showerror("Ошибка", "Пользователь с таким логином уже существует!")

        elif err[0] == "empty": messagebox.showerror("Ошибка", "Поле \""+ err[1] +"\" не может быть пустым!"); return False
        elif err[0] == "spaces": messagebox.showerror("Ошибка", "В поле \"" + err[1] + "\" не могут находиться пробелы!"); return False
        elif err[0] == "length": messagebox.showerror("Ошибка", "Поле \"" + err[1] + "\" не может содержать более 32 символов!"); return False

class CreateNewDoctorForm:
    def __init__(self, parentWindow, UserID):
        self.UserID = UserID
        self.root = Toplevel(parentWindow)
        self.root.title("[НЕ РАБОТАЕТ]Создание нового доктора")
        self.root.geometry("320x275")

        # self.root.iconbitmap("anime.ico")
        self.root.resizable(width = False, height = False)
        #self.root.wm_attributes("-topmost", 1)
        self.root.config(bg = "#FFF")


        #variables
        self.Name = StringVar()
        self.Surname = StringVar()
        self.Lastname = StringVar()
        self.Profile = StringVar()
        self.Workdays = StringVar()
        self.Worktime_start = StringVar()
        self.Worktime_end = StringVar()
        self.vacation = StringVar()

        self.lbl_title = ("Имя:", "Фамилия:", "Отчество:", "Специальность:", "Дни работы:", "Начало работы:", "Окончание работы:")
        for lbl in range(0,len(self.lbl_title)):
            self.lbl = Label(self.root, text=self.lbl_title[lbl], font=entry_font, background="#FFF").place(x=10, y = 10+31*lbl)

        self.NameEntry = Entry(self.root, font=entry_font, textvariable = self.Name, background=entry_color).place(x=110, y = 50-40, width = 200)
        self.SurnameEntry = Entry(self.root, font=entry_font, textvariable = self.Surname, background=entry_color).place(x=110, y = 81-40, width = 200)
        self.LastnameEntry = Entry(self.root, font=entry_font, textvariable = self.Lastname, background=entry_color).place(x=110, y = 112-40, width = 200)
        self.AddressEntry = Entry(self.root, font=entry_font, textvariable = self.Address, background=entry_color).place(x=110, y = 143-40, width = 200)
        self.BlockEntry = ttk.Combobox(self.root, state="readonly", values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"], font=entry_font, textvariable = self.Block, background=entry_color).place(x=110, y = 174-40, width = 200)
        self.MedicalIDEntry = Entry(self.root, font=entry_font, textvariable = self.MedicalID, background=entry_color).place(x=110, y = 205-40, width = 200)
        self.PassportEntry = Entry(self.root, font=entry_font, textvariable = self.Passport, background=entry_color).place(x=110, y = 236-40, width = 200)
        #
        # self.GenPassword = Button(self.root, text = "Ген.", command = lambda:self.Password.set(Password_Generator())).place(x=285, y=196, width=25, height=22)
        # self.ButtonSubmit = Button(self.root, text = "Создать", font=entry_font, command = self.edit_info).place(x=70, y=230)
        # self.ButtonCancel = Button(self.root, text = "Отмена", font=entry_font, command = lambda:self.root.destroy()).place(x=170, y=230)
        #
        # self.grab_focus()

class ChangePasswordWindow: #Создание новой анкеты клиента
    def __init__(self, parentWindow, executorID, userID):
        self.UserID = userID
        self.ExecutorID = executorID
        self.root = Toplevel(parentWindow)
        self.root.title("Изменение пароля")
        self.root.geometry("310x125")
        self.x = (self.root.winfo_screenwidth()) / 2 - self.root.winfo_reqwidth()
        self.y = (self.root.winfo_screenheight()) / 2 - self.root.winfo_reqheight()
        self.root.geometry("+%d+%d" % (self.x, self.y))
        # self.root.iconbitmap("anime.ico")
        self.root.resizable(width = False, height = False)
        self.root.config(bg = "#FFF")

        self.password = StringVar()
        self.repeat_password = StringVar()


        self.LoginLabel = Label(self.root, text="Новый пароль", font=entry_font, background="#FFF").place(x=10, y=10)
        self.PasswordEntry = Entry(self.root, textvariable=self.password)
        self.PasswordEntry.place(x=150, y=10, width=150, height=25)

        Label(self.root, text="Повторите пароль", font=entry_font, background="#FFF").place(x=10, y=50)
        self.RepeatPasswordEntry = Entry(self.root, textvariable=self.repeat_password)
        self.RepeatPasswordEntry.place(x=150, y=50, width=150, height=25)

        Button(self.root, text="Сохранить", font=entry_font, command=self.Submit).place(x=10, y=85, width = 90)
        Button(self.root, text="Отмена", font=entry_font, command= lambda:self.root.destroy()).place(x=105, y=85, width = 80)
        Button(self.root, text="Генерировать", font=entry_font, command= self.gen_pass).place(x=190, y=85, width = 110)

        self.grab_focus()

    def grab_focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()

    def run(self):#
        self.root.mainloop()#

    def gen_pass(self):
        password = Password_Generator()
        self.password.set(password)
        self.repeat_password.set(password)

    def Submit(self):
        if self.password.get() == self.repeat_password.get():
            if len(self.password.get()) >= 8:
                if CHANGE_PASSWORD(self.ExecutorID, self.UserID, self.password.get()):
                    messagebox.showinfo("Успех!", "Пароль умпешно изменен!")
                    self.root.destroy()
                else:
                    messagebox.showerror("Ошибка","Пароль изменить не удалось.")
            else:
                messagebox.showinfo("Ошибка", "Пароль должен содержать минимум 8 символов.")

if __name__ == "__main__":
    new_window = LoginWindow()

    #new_window = MainWindow(LOGIN_WORKER("root", "root"))

    new_window.run()