#Create a app banking statement with help python tkinter or SQL lite 
# this is the welcome page of the app
import tkinter as tk#this is the basic things
root=tk.Tk()
root.title("Kailash Bank") 
root.geometry("800x700")
#the tittle of the window
tittle=tk.Label(root,text="WELCOME TO KAILASH BANK",
                    font=("Arila",20,"bold"),              
                    bg="#f0f0f0",fg="#333333")
tittle.pack(pady=20)
root.mainloop()