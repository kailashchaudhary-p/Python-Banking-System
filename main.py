from tkinter import *
from tkinter import messagebox
import sqlite3
import subprocess
import os

# ---------- DATABASE SETUP ----------
def init_db():
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        account_no TEXT,
        password TEXT,
        balance REAL
    )
    """)

    # default user
    cursor.execute("SELECT * FROM users WHERE username='user1'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO users (username, account_no, password, balance) VALUES (?,?,?,?)",
                       ("user1", "12345", "123", 5000))

    conn.commit()
    conn.close()

# ---------- WELCOME PAGE ----------
class WelcomePage:
    def __init__(self):
        self.root = Tk()
        self.root.title("Banking System")
        self.root.geometry("900x500")

        Label(self.root, text="Welcome to Banking System", font=("Arial", 24)).pack(pady=50)

       
        Button(self.root, text="User Login", command=self.user_login, width=20).pack(pady=20)

        self.root.mainloop()

   

    def user_login(self):
        self.root.destroy()
        UserLogin()



   
# ---------- USER LOGIN ----------
class UserLogin:
    def __init__(self):
        self.root = Tk()
        self.root.title("User Login")
        self.root.geometry("400x350")

        Label(self.root, text="User Login", font=("Arial", 18)).pack(pady=20)

        self.username = Entry(self.root)
        self.username.pack(pady=10)

        self.acc = Entry(self.root)
        self.acc.pack(pady=10)

        self.password = Entry(self.root, show="*")
        self.password.pack(pady=10)

        Button(self.root, text="Login", command=self.login).pack(pady=20)

        self.root.mainloop()

    def login(self):
        conn = sqlite3.connect("bank.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username=? AND account_no=? AND password=?",
                       (self.username.get(), self.acc.get(), self.password.get()))
        user = cursor.fetchone()
        conn.close()

        if user:
            # session save
            with open("session.txt", "w") as f:
                f.write(self.acc.get())

            messagebox.showinfo("Success", "Login Successful")
            self.root.destroy()
            subprocess.run(["python", "user_dashboard.py"])
        else:
            messagebox.showerror("Error", "Invalid Details")

# ---------- RUN ----------
if __name__ == "__main__":
    init_db()
    WelcomePage()