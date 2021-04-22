from tkinter import *

window = Tk()
#generating window title
window.title("My first python application")
#creating a label widget
myLabel1 = Label(window, text = "hello Aditya")
myLabel2 = Label(window, text = "hello Aastha")
# --putting it on the screen--

#grid system layout
#it will layout the widgets in grid pattern with row and column
#it works as a relative layout in android studio
myLabel2.grid(row=0, column=0)
myLabel1.grid(row=1,column=0)

window.mainloop()