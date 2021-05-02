#in this program we will create multiple raddio buttons using for loop
#this program shows you how to use radio buttons (Buttons with a tick mark for selecting things in a form)
from tkinter import *
from PIL import ImageTk,Image

window = Tk()
window.title("this application demonstrates how to put multiple radio buttons using for loop")

MODES=[
("Pepperoni","Pepperoni"),
("Cheese","Cheese"),
("Mushroom","Mushroom"),
("Onion","Onion"),
]

pizza = StringVar() #tkinter string variable
pizza.set("Pepperoni")

#creating multiple radio buttons using for loop in the application
for text,modes in MODES:
    Radiobutton(window,text=text,variable=pizza,value = modes).pack(anchor=W)

def setR(val):
    myLabel = Label(window,text=val)
    myLabel.pack()

Button = Button(window,text="click",command=lambda :setR(pizza.get()))
Button.pack()

window.mainloop()