from tkinter import *
from tkinter import messagebox
import sqlite3
import os
from login import login_window
from create_account import create_account_window
from database import create_table

# DATABASE SETUP 
def init_db():
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        acc_no INTEGER PRIMARY KEY,
        name TEXT,
        pin TEXT,
        balance REAL
    )
    """)

    # default user
    cursor.execute("SELECT * FROM accounts WHERE name='User1'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO accounts (acc_no, name, pin, balance) VALUES (?,?,?,?)",
                       (10001, "User1", "1234", 5000))

    conn.commit()
    conn.close()

# WELCOME PAGE 
class WelcomePage:
    def __init__(self):
        self.root = Tk()
        self.root.title("Banking System")
        self.root.geometry("900x500")
        self.root.resizable(False, False)

        # Add background image or color
        try:
            # Try to load background image if it exists
            self.bg_image = PhotoImage(file='front_page.png')
            self.bg_label = Label(self.root, image=self.bg_image)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except:
            # Fallback to gradient background with color
            self.root.configure(bg='#1E3C72')
            self.bg_label = Label(self.root, bg='#1E3C72')
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Title with white text
        title_label = Label(self.root, text="Welcome to Banking System", 
                          font=("Arial", 28, "bold"), 
                          bg='#1E3C72' if not hasattr(self, 'bg_image') else '', 
                          fg='white')
        title_label.pack(pady=50)

        # Login Button
        login_btn = Button(self.root, text="User Login", command=self.user_login, 
                          width=20, font=("Arial", 12), 
                          bg='#2A5298', fg='white', 
                          padx=10, pady=10)
        login_btn.pack(pady=15)

        # Create Account Button
        create_btn = Button(self.root, text="Create Account", command=self.create_account, 
                           width=20, font=("Arial", 12), 
                           bg='#2A5298', fg='white', 
                           padx=10, pady=10)
        create_btn.pack(pady=15)

        # Exit Button
        exit_btn = Button(self.root, text="Exit", command=self.root.quit, 
                         width=20, font=("Arial", 12), 
                         bg='#C41E3A', fg='white', 
                         padx=10, pady=10)
        exit_btn.pack(pady=15)

        self.root.mainloop()

    def user_login(self):
        self.root.withdraw()
        login_window(self.root)

    def create_account(self):
        self.root.withdraw()
        create_account_window(self.root)




# RUN 
if __name__ == "__main__":
    init_db()
    create_table()
    WelcomePage()