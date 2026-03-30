import tkinter as tk
from tkinter import messagebox
from database import cursor
from dashboard import open_dashboard
import random

def login_window(root):

    def check_login():
        acc_no = entry_acc.get()
        pin = entry_pin.get()

        cursor.execute("SELECT * FROM accounts WHERE acc_no=? AND pin=?",
                       (acc_no, pin))
        user = cursor.fetchone()

        if user:
            generate_otp(user)
        else:
            messagebox.showerror("Error", "Invalid Details")

    def generate_otp(user):
        otp = random.randint(1000, 9999)

        messagebox.showinfo("OTP", f"Your OTP is: {otp}")  # demo purpose

        otp_window(user, otp)

    def otp_window(user, real_otp):
        win = tk.Toplevel(root)
        win.title("Enter OTP")

        tk.Label(win, text="Enter OTP").pack()
        entry_otp = tk.Entry(win)
        entry_otp.pack()

        def verify_otp():
            if entry_otp.get() == str(real_otp):
                messagebox.showinfo("Success", "Login Successful")
                win.destroy()
                open_dashboard(root, user)
            else:
                messagebox.showerror("Error", "Wrong OTP")

        tk.Button(win, text="Verify", command=verify_otp).pack()

    win = tk.Toplevel(root)
    win.title("Login")

    tk.Label(win, text="Account No").pack()
    entry_acc = tk.Entry(win)
    entry_acc.pack()

    tk.Label(win, text="PIN").pack()
    entry_pin = tk.Entry(win, show="*")
    entry_pin.pack()

    tk.Button(win, text="Login", command=check_login).pack()