import tkinter as tk

class AddNewAccount:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Kailash Bank - Create Account")
        self.root.geometry("1500x900")

        # Background Image
        # self.bg_image = tk.PhotoImage(file="1768579.jpg")
        # self.bg = tk.Label(self.root, image=self.bg_image)
        # self.bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Main Frame (Form)
        self.frame = tk.Frame(self.root, bg="black")
        self.frame.place(x=550, y=200, width=400, height=450)

        # Title
        title = tk.Label(self.frame, text="Create New Account",
                         font=("Arial", 18, "bold"), bg="white")
        title.pack(pady=20)

        # Name
        name_label = tk.Label(self.frame, text="Full Name",
                              font=("Arial", 12), bg="white")
        name_label.pack()
        self.name_entry = tk.Entry(self.frame, width=30)
        self.name_entry.pack(pady=5)

        # Mobile
        mobile_label = tk.Label(self.frame, text="Mobile Number",
                                font=("Arial", 12), bg="white")
        mobile_label.pack()
        self.mobile_entry = tk.Entry(self.frame, width=30)
        self.mobile_entry.pack(pady=5)

        # Address
        address_label = tk.Label(self.frame, text="Address",
                                 font=("Arial", 12), bg="white")
        address_label.pack()
        self.address_entry = tk.Entry(self.frame, width=30)
        self.address_entry.pack(pady=5)

        # Password
        password_label = tk.Label(self.frame, text="Password",
                                  font=("Arial", 12), bg="white")
        password_label.pack()
        self.password_entry = tk.Entry(self.frame, width=30, show="*")
        self.password_entry.pack(pady=5)

        # Button
        create_btn = tk.Button(self.frame, text="Create Account",
                               bg="green", fg="white",
                               font=("Arial", 12, "bold"),
                               width=20, command=self.create_account)
        create_btn.pack(pady=30)

        self.root.mainloop()

    def create_account(self):
        name = self.name_entry.get()
        mobile = self.mobile_entry.get()
        address = self.address_entry.get()
        password = self.password_entry.get()
        print(f"Account created: Name={name}, Mobile={mobile}, Address={address}, Password={password}")


obj = AddNewAccount()