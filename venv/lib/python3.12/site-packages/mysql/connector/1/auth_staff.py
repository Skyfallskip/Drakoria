import tkinter as tk
from tkinter import messagebox
from db import connect  # ← Подключение к базе данных
from screens_admin import admin_screen
from screens_manager import manager_screen
from screens_staff import staff_screen

def show_staff_login(root):
    win = tk.Toplevel(root)
    win.title("Вход (Персонал)")

    tk.Label(win, text="Логин").pack()
    login_entry = tk.Entry(win)
    login_entry.pack()

    tk.Label(win, text="Пароль").pack()
    password_entry = tk.Entry(win, show="*")
    password_entry.pack()

    def login():
        login = login_entry.get()
        password = password_entry.get()

        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT password, role FROM users WHERE login = %s", (login,))
        # Поменять при смене БД:
        # - users → таблица с персоналом
        # - login → поле логина
        # - password → поле с паролем
        # - role → поле с ролью сотрудника

        result = cursor.fetchone()
        conn.close()

        if not result or result["password"] != password:
            messagebox.showerror("Ошибка", "Неверный логин или пароль")
            return

        messagebox.showinfo("Успех", f"Добро пожаловать, {result['role']}")
        # ↑ role — поле с ролью (Admin, Manager, Staff)
        win.destroy()

        if result["role"] == "Admin":
            admin_screen()
        elif result["role"] == "Manager":
            manager_screen()
        elif result["role"] == "Staff":
            staff_screen()

    tk.Button(win, text="Войти", command=login).pack()
