from tkinter import *

window = Tk()

#how can make our buttons to do something when we click it
def myclick1():
	myLabel = Label(window,text="you clicked button 1")
	myLabel.grid(row=3,column=0)
def myclick3():
	myLabel = Label(window,text="you clicked button 3")
	myLabel.grid(row=4,column=0)
def myclick4():
	myLabel = Label(window,text="you clicked button 4")
	myLabel.grid(row=5,column=0)
def myclick5():
	myLabel = Label(window,text="you clicked button 5")
	myLabel.grid(row=6,column=0)

#creating widgets and GUI window components
#generating window title
window.title("My first python application")
#creating a button 
# command = myfunctionName will allow us to make our button do anything by creating a custom function for our buttons 
myButton = Button(window, text="click me!!",command = myclick1)
#how to use state to disable or enable button click feature
myButton2 = Button(window,text = "click me 2!!",state=DISABLED)
#how to change size of a button
#padx will increase the size of a button along x axis and pady will increase the size of a button along y axis
myButton3 = Button(window, text = "click me 3!!", padx = 70, pady=70,command = myclick3)
#fg will allow us to use custom colors on the text of a button
#bg will allow us to use custom color on the buttons background  
#you can also use hexColor codes
myButton4 = Button(window, text = "click me 3!!", padx = 70,command = myclick4, fg = "RED", bg = "Yellow")
myButton5 = Button(window, text = "click me 3!!", pady=70,command = myclick5)

# --putting widets and GUI window components on the screen--
#putting button on screen
myButton.grid(row=0, column=0)
myButton2.grid(row=1,column=0)
myButton3.grid(row=2,column=0)
myButton4.grid(row=0,column=1)
myButton5.grid(row=1,column=1)

window.mainloop()