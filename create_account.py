import tkinter as tk
from tkinter import messagebox
from database import cursor, conn

def create_account_window(root):

    def save_account():
        acc_no = entry_acc.get()
        name = entry_name.get()
        pin = entry_pin.get()
        balance = entry_balance.get()

        if not acc_no or not name or not pin or not balance:
            messagebox.showerror("Error", "Please fill all fields")
            return

        # Check if account number already exists
        cursor.execute("SELECT * FROM accounts WHERE acc_no=?", (acc_no,))
        if cursor.fetchone():
            messagebox.showerror("Error", "Account Number already exists!")
            return

        try:
            acc_no = int(acc_no)
            balance = float(balance)
            if balance < 0:
                messagebox.showerror("Error", "Balance cannot be negative")
                return
        except ValueError:
            messagebox.showerror("Error", "Account Number and Balance must be numbers")
            return

        if len(pin) < 4:
            messagebox.showerror("Error", "PIN must be at least 4 digits")
            return

        try:
            cursor.execute("INSERT INTO accounts(acc_no, name, pin, balance) VALUES(?,?,?,?)",
                           (acc_no, name, pin, balance))
            conn.commit()

            messagebox.showinfo("Success", f"Account Created Successfully!\n\nAccount Number: {acc_no}\nName: {name}\nBalance: Rs. {balance:.2f}")
            entry_acc.delete(0, tk.END)
            entry_name.delete(0, tk.END)
            entry_pin.delete(0, tk.END)
            entry_balance.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create account: {str(e)}")

    win = tk.Toplevel(root)
    win.title("Create Account")
    win.geometry("450x450")

    tk.Label(win, text="Create New Account", font=("Arial", 18, "bold"), fg='#1E3C72').pack(pady=20)

    tk.Label(win, text="Account Number", font=("Arial", 10)).pack(pady=5)
    entry_acc = tk.Entry(win, font=("Arial", 10))
    entry_acc.pack(pady=5)

    tk.Label(win, text="Full Name", font=("Arial", 10)).pack(pady=5)
    entry_name = tk.Entry(win, font=("Arial", 10))
    entry_name.pack(pady=5)

    tk.Label(win, text="PIN (4+ digits)", font=("Arial", 10)).pack(pady=5)
    entry_pin = tk.Entry(win, show="*", font=("Arial", 10))
    entry_pin.pack(pady=5)

    tk.Label(win, text="Initial Balance (Rs.)", font=("Arial", 10)).pack(pady=5)
    entry_balance = tk.Entry(win, font=("Arial", 10))
    entry_balance.pack(pady=5)

    tk.Button(win, text="Create Account", command=save_account, 
             font=("Arial", 11), bg='#2A5298', fg='white',
             width=20, pady=10).pack(pady=20)