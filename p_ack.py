from tkinter import *

window = Tk()
#generating window title
window.title("My first python application")
#creating a label widget
myLabel1 = Label(window, text = "hello Aditya")
myLabel2 = Label(window, text = "hello Aastha")
# --putting it on the screen--
#pack function will pack the widget and wrap the window according the size of the widget
#window size will depend on the size of the widgets inside the window when we use pack function
myLabel1.pack()

window.mainloop()