import tkinter as tk

def show_client_screen():
    win = tk.Toplevel()
    win.title("Панель клиента")

    tk.Label(win, text="Вы вошли как клиент", font=("Arial", 14)).pack(pady=20)

    # Пример кнопок-заглушек
    tk.Button(win, text="Посмотреть бронирование", width=30).pack(pady=5)
    tk.Button(win, text="Посмотреть оплату", width=30).pack(pady=5)