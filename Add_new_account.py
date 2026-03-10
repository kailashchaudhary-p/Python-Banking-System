#for new account creation
import tkinter as tk
class add_new_account:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("kailash bank")
        self.root.geometry("1500x1200")
        #background immage
        image=tk.PhotoImage(file=("ChatGPT Image Mar 9, 2026, 09_53_21 PM.png"))
        self.background=tk.Label(self.root,image=image)
        self.background.place(x=0,y=0)








        self.root.mainloop()
obj=add_new_account()