#this program shows you how to use pop up window in our application
from tkinter import *
from PIL import ImageTk,Image
#import message box to create a pop up window of information display type
from tkinter import messagebox

window = Tk()
window.title("how to create a pop up window")

def popup():
    #create a message box showinfo will just show some kind of information on the pop up window it is not interactive
    #showinfo("the title bar that you want to show up", message that you want to show in your actual pop up window)
    messagebox.showinfo("developer info", "Name = Aditya Kumar \n class = B.tech 2nd year \n college = SITM")

Button = Button(window,text="pop up window",command = popup).pack()

window.mainloop()