import tkinter as tk
from tkinter import messagebox
from db import connect  # ← Подключение к базе данных
import bcrypt
from screens_client import show_client_screen  # Экран после успешного входа

login_attempts = {}  # Для отслеживания количества неудачных попыток входа

def show_login(root):
    win = tk.Toplevel(root)
    win.title("Вход (Клиент)")

    tk.Label(win, text="Логин").pack()
    login_entry = tk.Entry(win)
    login_entry.pack()

    tk.Label(win, text="Пароль").pack()
    password_entry = tk.Entry(win, show="*")
    password_entry.pack()

    def attempt_login():
        login = login_entry.get()
        password = password_entry.get()

        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM client WHERE login = %s", (login,))
        # Поменять при смене БД:
        # - client → название таблицы с клиентами
        # - login → поле логина
        # - password → поле с хешированным паролем

        result = cursor.fetchone()
        conn.close()

        if not result:
            messagebox.showerror("Ошибка", "Пользователь не найден")
            return

        if login in login_attempts and login_attempts[login] >= 3:
            messagebox.showerror("Ошибка", "Учетная запись заблокирована")
            return

        if bcrypt.checkpw(password.encode(), result['password'].encode()):
            messagebox.showinfo("Успех", "Вы успешно вошли")
            login_attempts.pop(login, None)
            win.destroy()
            show_client_screen()
        else:
            login_attempts[login] = login_attempts.get(login, 0) + 1
            messagebox.showerror("Ошибка", "Неверный пароль")

    tk.Button(win, text="Войти", command=attempt_login).pack()

def show_register(root):
    win = tk.Toplevel(root)
    win.title("Регистрация")

    entries = {}
    for label in ("Имя", "Фамилия", "Отчество", "Логин", "Пароль"):
        tk.Label(win, text=label).pack()
        e = tk.Entry(win, show="*" if label == "Пароль" else None)
        e.pack()
        entries[label] = e

    def register():
        data = {k: v.get() for k, v in entries.items()}
        if not all(data.values()):
            messagebox.showerror("Ошибка", "Заполните все поля")
            return

        conn = connect()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id_client FROM client
            WHERE first_name_client=%s AND last_name_client=%s AND father_name_client=%s
        """, (data["Имя"], data["Фамилия"], data["Отчество"]))
        # Поменять при смене БД:
        # - client → таблица с клиентами
        # - id_client → идентификатор клиента
        # - first_name_client, last_name_client, father_name_client → поля для поиска по ФИО

        existing = cursor.fetchone()

        hashed = bcrypt.hashpw(data["Пароль"].encode(), bcrypt.gensalt()).decode()

        if existing:
            cursor.execute("UPDATE client SET login=%s, password=%s WHERE id_client=%s",
                           (data["Логин"], hashed, existing['id_client']))
            # Поменять:
            # - client → таблица
            # - login, password → поля для обновления
            # - id_client → идентификатор
        else:
            cursor.execute("""
                INSERT INTO client (first_name_client, last_name_client, father_name_client, login, password)
                VALUES (%s, %s, %s, %s, %s)
            """, (data["Имя"], data["Фамилия"], data["Отчество"], data["Логин"], hashed))
            # Поменять:
            # - client → таблица
            # - все поля → имена колонок в новой БД

        conn.commit()
        conn.close()
        messagebox.showinfo("Успех", "Регистрация завершена")
        win.destroy()
        show_client_screen()

    tk.Button(win, text="Зарегистрироваться", command=register).pack()
