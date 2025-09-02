import tkinter as tk

def admin_screen():
    win = tk.Toplevel()
    win.title("Админ-панель")

    for label in ("Все бронирования", "Номерной фонд", "Постояльцы гостиницы"):
        tk.Button(win, text=label, width=30).pack(pady=5)
