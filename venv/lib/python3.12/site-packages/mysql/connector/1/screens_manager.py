import tkinter as tk

def manager_screen():
    win = tk.Toplevel()
    win.title("Панель менеджера")

    for label in ("Посмотреть статистику", "Посмотреть выручку", "Наполненность номеров"):
        tk.Button(win, text=label, width=30).pack(pady=5)
