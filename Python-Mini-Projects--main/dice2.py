from tkinter import * 
import random
#pip install Pillow
from PIL import Image,ImageTk

root=Tk()
root.title("Dice Simulator")
root.geometry("600x500")
dice=["1.jpg","2.png","3.jpg","4.png","5.jpg","6.jpg"]
diceimage=ImageTk.PhotoImage(Image.open(random.choice(dice)))
f=Label(image=diceimage)
f.image=diceimage
f.pack()

def dice_rolling():
    diceimage=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    f.configure(image=diceimage)
    f.image=diceimage
Btn=Button(root,text="Push me",
font=("Arial","30","italic"),command=dice_rolling,bg="yellow",fg="black")
Btn.pack()   
root.mainloop()