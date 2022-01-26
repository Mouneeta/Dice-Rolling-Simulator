#Tkinter is a Python module that is used to develop GUI applications 
from distutils.command.config import config
import random
from tkinter import * #import everything

root=Tk() #The root window is created.
root.geometry("600x300") #This method is used to set the dimensions of the Tkinter window and is used to set the position of the main window on the user's desktop.
text_1=Label(root,text='',font=("arial",300))
def roll_the_dice():
    num_code=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    text_1.config(text=f'{random.choice(num_code)}{random.choice(num_code)}')
    text_1.pack()
button_1=Button(root,text="Roll the dice",command=roll_the_dice)
button_1.place(x=250,y=0)

root.mainloop()