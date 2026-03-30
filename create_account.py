import tkinter as tk
from tkinter import messagebox
from database import cursor, conn

def create_account_window(root):

    def save_account():
        name = entry_name.get()
        pin = entry_pin.get()
        balance = entry_balance.get()

        cursor.execute("INSERT INTO accounts(name, pin, balance) VALUES(?,?,?)",
                       (name, pin, balance))
        conn.commit()

        messagebox.showinfo("Success", "Account Created")

    win = tk.Toplevel(root)
    win.title("Create Account")

    tk.Label(win, text="Name").pack()
    entry_name = tk.Entry(win)
    entry_name.pack()

    tk.Label(win, text="PIN").pack()
    entry_pin = tk.Entry(win, show="*")
    entry_pin.pack()

    tk.Label(win, text="Balance").pack()
    entry_balance = tk.Entry(win)
    entry_balance.pack()

    tk.Button(win, text="Create", command=save_account).pack()