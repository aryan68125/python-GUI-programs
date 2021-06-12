#this program demonstrates how to open new windows by clicking a button
#this program shows you how to use pop up window in our application
from tkinter import *

#if the import of ImageTk does't work then 
#type in terminal :- for python3.5 and above--> sudo apt-get install python3-pil python3-pil.imagetk
#this module allows us to use png and jpg images in our program
from PIL import ImageTk,Image

window = Tk()
window.title("how to create a new window")

#importing image to our program
#note this has to be done outside any function otherwise the import will not happen
#image5 = ImageTk.PhotoImage(Image.open("/home/aditya/development/python/imageViewer/icons/linux5.png"))

#creating a function that will create a new window
def open_a_new_window():
    window2 = Toplevel()
    my_label = Label(window2,text = "This a window 2")
    my_label.grid(row=0,column=0,padx=10,pady=10)
    open_image = Button(window2,text = "open image",command=open_image_in_a_new_window)
    open_image.grid(row=1,column=0,padx=10,pady=10)
    

def open_image_in_a_new_window():
   window3 = Toplevel()
   #importing image to our program
   #if you are importiong image inside the function then you need to declare image5 as a global variable
   global image5
   image5 = ImageTk.PhotoImage(Image.open("/home/aditya/development/python/imageViewer/icons/linux5.png"))
   #puttin image on the screen in our application
   my_lable = Label(window3,image=image5)
   my_lable.grid(row=0,column=0)
   

#creating a button that will open a new window
open_window = Button(window,text = "open a new window",command= open_a_new_window)
#putting the button on the window 1 screen called window
open_window.grid(row=0,column=0,padx=10,pady=10)

window.mainloop()