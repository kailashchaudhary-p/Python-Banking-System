import tkinter as tk
from tkinter import messagebox
from database import cursor, conn

def open_dashboard(root, user):

    dash = tk.Toplevel(root)
    dash.title("Dashboard")

    acc_no = user[0]

    def check_balance():
        cursor.execute("SELECT balance FROM accounts WHERE acc_no=?", (acc_no,))
        bal = cursor.fetchone()[0]
        messagebox.showinfo("Balance", f"Balance: {bal}")

    def deposit():
        amount = float(entry_amount.get())
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE acc_no=?",
                       (amount, acc_no))
        conn.commit()
        messagebox.showinfo("Success", "Deposited")

    def withdraw():
        amount = float(entry_amount.get())

        cursor.execute("SELECT balance FROM accounts WHERE acc_no=?", (acc_no,))
        bal = cursor.fetchone()[0]

        if amount > bal:
            messagebox.showerror("Error", "Insufficient Balance")
        else:
            cursor.execute("UPDATE accounts SET balance = balance - ? WHERE acc_no=?",
                           (amount, acc_no))
            conn.commit()
            messagebox.showinfo("Success", "Withdrawn")

    tk.Label(dash, text="Enter Amount").pack()
    entry_amount = tk.Entry(dash)
    entry_amount.pack()

    tk.Button(dash, text="Check Balance", command=check_balance).pack()
    tk.Button(dash, text="Deposit", command=deposit).pack()
    tk.Button(dash, text="Withdraw", command=withdraw).pack()