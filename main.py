import tkinter as tk
from database import create_table
from create_account import create_account_window
from login import login_window

create_table()

root = tk.Tk()
root.title("Banking App")

# ✅ Full screen
root.state('zoomed')   # Windows ke liye best

# (Alternative method)
# root.geometry("1200x700")

tk.Label(root, text="Banking System", font=("Arial", 24, "bold")).pack(pady=20)

tk.Button(root, text="Create Account", width=25, height=2,
          command=lambda: create_account_window(root)).pack(pady=10)

tk.Button(root, text="Login", width=25, height=2,
          command=lambda: login_window(root)).pack(pady=10)

root.mainloop()