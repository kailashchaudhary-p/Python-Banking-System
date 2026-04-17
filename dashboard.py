import tkinter as tk
from tkinter import messagebox
from database import cursor, conn

def open_dashboard(root, user):

    dash = tk.Toplevel(root)
    dash.title("Dashboard")
    dash.geometry("500x500")

    acc_no = user[0]
    user_name = user[1]

    # Display user info
    tk.Label(dash, text=f"Welcome, {user_name}!", 
            font=("Arial", 16, "bold"), fg='#1E3C72').pack(pady=10)
    tk.Label(dash, text=f"Account Number: {acc_no}", 
            font=("Arial", 11), fg='gray').pack(pady=5)

    def check_balance():
        try:
            cursor.execute("SELECT balance FROM accounts WHERE acc_no=?", (acc_no,))
            result = cursor.fetchone()
            if result:
                bal = result[0]
                messagebox.showinfo("Balance", f"Your Current Balance: Rs. {bal:.2f}")
            else:
                messagebox.showerror("Error", "Account not found")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

    def deposit():
        try:
            amount = float(entry_amount.get())
            if amount <= 0:
                messagebox.showerror("Error", "Amount must be greater than 0")
                return
            
            cursor.execute("UPDATE accounts SET balance = balance + ? WHERE acc_no=?",
                           (amount, acc_no))
            conn.commit()
            messagebox.showinfo("Success", f"Rs. {amount:.2f} Deposited Successfully!")
            entry_amount.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

    def withdraw():
        try:
            amount = float(entry_amount.get())
            if amount <= 0:
                messagebox.showerror("Error", "Amount must be greater than 0")
                return

            cursor.execute("SELECT balance FROM accounts WHERE acc_no=?", (acc_no,))
            result = cursor.fetchone()
            if result:
                bal = result[0]

                if amount > bal:
                    messagebox.showerror("Error", f"Insufficient Balance! Current Balance: Rs. {bal:.2f}")
                else:
                    cursor.execute("UPDATE accounts SET balance = balance - ? WHERE acc_no=?",
                                   (amount, acc_no))
                    conn.commit()
                    messagebox.showinfo("Success", f"Rs. {amount:.2f} Withdrawn Successfully!")
                    entry_amount.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Account not found")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

    # Amount entry
    tk.Label(dash, text="Enter Amount", font=("Arial", 11, "bold")).pack(pady=10)
    entry_amount = tk.Entry(dash, font=("Arial", 12), width=25)
    entry_amount.pack(pady=5)

    # Buttons
    button_frame = tk.Frame(dash)
    button_frame.pack(pady=20)

    tk.Button(button_frame, text="Check Balance", command=check_balance, 
             font=("Arial", 10), bg='#2A5298', fg='white',
             width=18, pady=8).pack(pady=5)
    tk.Button(button_frame, text="Deposit", command=deposit, 
             font=("Arial", 10), bg='#28A745', fg='white',
             width=18, pady=8).pack(pady=5)
    tk.Button(button_frame, text="Withdraw", command=withdraw, 
             font=("Arial", 10), bg='#FFC107', fg='black',
             width=18, pady=8).pack(pady=5)
    tk.Button(button_frame, text="Logout", command=dash.destroy, 
             font=("Arial", 10), bg='#C41E3A', fg='white',
             width=18, pady=8).pack(pady=5)