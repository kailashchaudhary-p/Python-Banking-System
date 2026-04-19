import tkinter as tk
from tkinter import messagebox
from database import cursor, conn
from dashboard import open_dashboard
import random

def login_window(root):

    def add_back_button(window, previous):
        tk.Button(window, text="← Back", command=lambda: [window.destroy(), previous.deiconify()],
                  font=("Arial", 10), bg='#2A5298', fg='white').place(relx=0.98, rely=0.03, anchor='ne')

    def check_login():
        acc_no = entry_acc.get()
        pin = entry_pin.get()

        if not acc_no or not pin:
            messagebox.showerror("Error", "Please fill all fields")
            return

        cursor.execute("SELECT * FROM accounts WHERE acc_no=? AND pin=?", (acc_no, pin))
        user = cursor.fetchone()

        if user:
            generate_otp(user)
        else:
            messagebox.showerror("Error", "Invalid Account Number or PIN")

    def generate_otp(user):
        otp = random.randint(1000, 9999)
        messagebox.showinfo("OTP", f"Your OTP is: {otp}\n(Demo Purpose)")
        otp_window(user, otp)

    def otp_window(user, real_otp):
        login_win.withdraw()
        otp_win = tk.Toplevel(root)
        otp_win.title("Enter OTP")
        otp_win.geometry("300x150")
        otp_win.protocol("WM_DELETE_WINDOW", lambda: [otp_win.destroy(), login_win.deiconify()])
        add_back_button(otp_win, login_win)

        tk.Label(otp_win, text="Enter OTP", font=("Arial", 12)).pack(pady=10)
        entry_otp = tk.Entry(otp_win, font=("Arial", 12))
        entry_otp.pack(pady=5)

        def verify_otp():
            if entry_otp.get() == str(real_otp):
                messagebox.showinfo("Success", "Login Successful")
                otp_win.destroy()
                login_win.destroy()
                open_dashboard(root, user)
            else:
                messagebox.showerror("Error", "Wrong OTP")

        tk.Button(otp_win, text="Verify", command=verify_otp,
                 font=("Arial", 10), bg='#2A5298', fg='white').pack(pady=10)

    root.withdraw()
    login_win = tk.Toplevel(root)
    login_win.title("Login")
    login_win.geometry("400x300")
    login_win.protocol("WM_DELETE_WINDOW", lambda: [login_win.destroy(), root.deiconify()])
    add_back_button(login_win, root)

    tk.Label(login_win, text="Login", font=("Arial", 18, "bold")).pack(pady=20)

    tk.Label(login_win, text="Account Number", font=("Arial", 10)).pack(pady=5)
    entry_acc = tk.Entry(login_win, font=("Arial", 10))
    entry_acc.pack(pady=5)

    tk.Label(login_win, text="PIN", font=("Arial", 10)).pack(pady=5)
    entry_pin = tk.Entry(login_win, show="*", font=("Arial", 10))
    entry_pin.pack(pady=5)

    tk.Button(login_win, text="Login", command=check_login,
             font=("Arial", 11), bg='#2A5298', fg='white',
             width=20, pady=10).pack(pady=20)
