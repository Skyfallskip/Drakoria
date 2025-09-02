import tkinter as tk
from auth_client import show_register, show_login
from auth_staff import show_staff_login

def main():
    root = tk.Tk()
    root.title("Гостиничная система")
    root.geometry("300x250")
    root.resizable(False, False)

    tk.Label(root, text="Добро пожаловать!", font=("Arial", 16)).pack(pady=20)

    tk.Button(root, text="Вход", width=25, command=lambda: show_login(root)).pack(pady=5)
    tk.Button(root, text="Регистрация", width=25, command=lambda: show_register(root)).pack(pady=5)
    tk.Button(root, text="Для персонала", width=25, command=lambda: show_staff_login(root)).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
