from tkinter import * 
import random

root=Tk()
root.title("Dice Simulator")
root.geometry("600x500")

f=Label(root,text="",font=("Arial","250","bold"),fg="red")
def rolling():
    dicelist=["\u2680","\u2681","\u2682","\u2683","\u2684","\u2685",]
    f.configure(text=f"{random.choice(dicelist)}")
    f.pack()
b=Button(root,text="Push me",font=("Arial","30","italic"),command=rolling)
b.pack()
root.mainloop()