from tkinter import *

window = Tk()

#how can make our buttons to do something when we click it
#how can make our buttons to do something when we click it
def myclick1():
	#inputFieldName.get() will allow us to extract the text entered by the user in the input field
	myLabel = Label(window,text=entry.get())
	myLabel.grid(row=3,column=0)

#creating widgets and GUI window components
#generating window title
window.title("My first python application")
#creating an input field like editText in android in application
#we can use width to increase the width of the input field
#you can use fg and bg to change the color of the input field just like in buttons
entry = Entry(window, width = 65)
myButton = Button(window, text="click me!!",command = myclick1)

# --putting widets and GUI window components on the screen--
entry.grid(row=0,column=0)
myButton.grid(row=1, column=0)


window.mainloop()