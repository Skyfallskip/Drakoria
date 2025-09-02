import tkinter as tk

def staff_screen():
    win = tk.Toplevel()
    win.title("Сотрудник")

    tk.Button(win, text="График уборки", width=30).pack(pady=20)
