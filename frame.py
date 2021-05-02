#adding frames to your python programs
from tkinter import *
from PIL import ImageTk,Image

window = Tk()
window.title("add Frames to your python application")

#frame is a widhet so it can be used like any other widget
#padx and pady here will pad the area inside the custom frame that the user has created
frame = LabelFrame(window,text="This is my custom frame",padx=5,pady=5)
#putting our cutom frame in our application on pur screen
#padx and pady will pad the area outside the custome frame that the user has created
frame.pack(padx=10,pady=10)

#now this time we won't be putting our button in window we will be putting our button in the frame that is 
#already inside the window of our application
button = Button(frame,text="click me!!")
button.grid(row=0,column=0,padx=10,pady=10)
button2 = Button(frame,text="click me!!")
button2.grid(row=1,column=0,padx=10,pady=10)

window.mainloop()