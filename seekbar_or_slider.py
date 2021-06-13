#this program demonstrates how to use slider or seekbar in your python tkinter application
from tkinter import *

window = Tk()
window.title("how to create a new window")

#function that gets the value of vertical seekbar
def verval():
    vaertical_label = Label(window,text = "vertical seekbar value "+ str(vertical.get()))
    vaertical_label.grid(row=0,column=2)
    #we can here set the size of our window
    window.geometry(str(vertical.get())+"x400")
#function that gets the value of horizontal seekbar
def horval():
    horizontal_label = Label(window,text = "horizontal seekbar value "+ str(horizontal.get()))
    horizontal_label.grid(row=1,column=2)
    #we can here set the size of our window
    window.geometry("400x"+str(horizontal.get()))

#creating a seekbar
vertical = Scale(window,from_=200,to=1000,orient=VERTICAL,)
vertical.grid(row=0,column=0)

horizontal = Scale(window,from_=200,to=1000,orient = HORIZONTAL)
horizontal.grid(row=1,column=0)

vertical_button = Button(window,text="get vertical seekbar value",command = verval)
vertical_button.grid(row=0,column=1)

horizontal_button = Button(window,text="get vertical seekbar value",command = horval)
horizontal_button.grid(row=1,column=1)
window.mainloop()