#this program shows you how to use radio buttons (Buttons with a tick mark for selecting things in a form)
from tkinter import *
from PIL import ImageTk,Image

window = Tk()
window.title("add Frames to your python application")

def setR(val):
    myLabel = Label(window,text=val)
    myLabel.pack()

#r and r2 are tkinter variable and not your typical python variable
#here we are going to declare r and r2 
r = IntVar()
r.set(2) #will set the variable r
Radiobutton(window,text="Option 1",variable = r,value=1,command = lambda: setR(r.get())).pack()
Radiobutton(window,text="Option 2",variable = r,value=2,command = lambda: setR(r.get())).pack()

myLabel = Label(window,text=r.get())
myLabel.pack()

window.mainloop()