import tkinter as tk
from login import login_window
from create_account import create_account_window, create_table

class Banking_app:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking App")
        self.root.geometry("1400x1250")

        create_table()

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(pady=40)

        tk.Label(self.main_frame, text="Welcome to Banking App", font=("Arial", 40)).grid(row=0, column=0, columnspan=2, pady=(0, 20))
        tk.Button(self.main_frame, text="Login", width=20, command=self.open_login).grid(row=10, column=0, columnspan=2, pady=10)
        tk.Button(self.main_frame, text="Create Account", width=20, command=self.open_create_account).grid(row=2, column=0, columnspan=2, pady=10)

    def open_login(self):
        login_window(self.root)

    def open_create_account(self):
        create_account_window(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = Banking_app(root)
    root.mainloop()