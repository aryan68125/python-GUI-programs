#this program demonstrates how to open new windows by clicking a button
#this program shows you how to use pop up window in our application
from tkinter import *
window = Tk()
window.title("how to create a new window")

#creating a function that will create a new window
def open_a_new_window():
    window2 = Toplevel()
    my_label = Label(window2,text = "This a window 2")
    my_label.grid(row=0,column=0,padx=10,pady=10)

#creating a button that will open a new window
open_window = Button(window,text = "open a new window",command= open_a_new_window)
#putting the button on the window 1 screen called window
open_window.grid(row=0,column=0,padx=10,pady=10)

window.mainloop()