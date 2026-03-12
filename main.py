#Create a app banking statement with help python tkinter or SQL lite 
# this is the welcome page of the app
import tkinter as tk#this is the basic things



class welcome_page:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Kailash Bank") 
        self.root.geometry("1500x1200")

        #background image 
        image=tk.PhotoImage(file="Screenshot_1.png")
        background=tk.Label(self.root,image=image)
        background.place(x=0,y=0)
       
         #TITTLE 
        tittle=tk.Label(self.root,text="WELCOME TO KAILASH BANK",
                    font=("Arila",20,"bold"),              
                    bg="#f0f0f0",fg="#333333")
        tittle.pack(pady=40)
        #Login button
        login_button=tk.Button(self.root,text="login",width=50)
        login_button.place(x=1100,y=600)
        #create new account button
        create_account=tk.Button(self.root,text="Create New Account",width=50)
        create_account.place(x=1100, y=400)
       
obj=welcome_page()