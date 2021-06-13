#how to open a open file dialog box using a button
#remember dialog box is not actually opening the file itself but it is actually returning the location of the file present in the filesystem of the linux
#opening of a file needs to be taken care of logically and programitcally
from tkinter import *

#if the import of ImageTk does't work then 
#type in terminal :- for python3.5 and above--> sudo apt-get install python3-pil python3-pil.imagetk
#this module allows us to use png and jpg images in our program
from PIL import ImageTk,Image

#inorder to use file dialogue box in our program we need to first import the dialogue box library
#this dialogue box library is a part of tkinter and not the part of python's core libraries
from tkinter import filedialog

window = Tk()
window.title("how to create a new window")

#the function below will handle the actual logic behind the button
def open_dialogue_box():
    #window.filename won't actually open a file it will just return the name of the file and the location of the file
    window.filename = filedialog.askopenfilename(initialdir ="/home/aditya/development/python/imageViewer/icons/", title="choose picture",filetypes=(("png files","*.png"),("all files","*.*")) )
    #importing image to our program
    #if you are importiong image inside the function then you need to declare image5 as a global variable
    global image5
    image5 = ImageTk.PhotoImage(Image.open(window.filename))
    #puttin image on the screen in our application
    my_lable = Label(window,image=image5)
    my_lable.grid(row=2,column=0)
def open_image_in_a_new_window():
   #window.filename won't actually open a file it will just return the name of the file and the location of the file
   window.filename = filedialog.askopenfilename(initialdir ="/home/aditya/development/python/imageViewer/icons/", title="choose picture",filetypes=(("png files","*.png"),("all files","*.*")) )
   window3 = Toplevel()
   #importing image to our program
   #if you are importiong image inside the function then you need to declare image5 as a global variable
   global image5
   image5 = ImageTk.PhotoImage(Image.open(window.filename))
   #puttin image on the screen in our application
   my_lable = Label(window3,image=image5)
   my_lable.grid(row=0,column=0)


#this button was created to open a fiule dialogue bax so that we can choose a file from our system's file manager
open_file_dialog_box = Button(window, text="open files",command= open_dialogue_box)
open_file_dialog_box.grid(row=0,column=0,padx=10,pady=10)

#this button will open the image in a new window
open_file_in_a_new_window = Button(window, text="open files in a new window",command= open_image_in_a_new_window)
open_file_in_a_new_window.grid(row=1,column=0,padx=10,pady=10)

window.mainloop()