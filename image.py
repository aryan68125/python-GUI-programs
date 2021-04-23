from tkinter import *
#if the import of ImageTk does't work then 
#type in terminal :- for python3.5 and above--> sudo apt-get install python3-pil python3-pil.imagetk
from PIL import ImageTk,Image
window = Tk()
window.title("Learn how to use icon, Images and Exit buttons")

#how to put an exit button on the window
Button_exit = Button(window, text="Exit Program", command=window.quit)
Button_exit.pack()

#how to deal with images in tkinter
my_image = ImageTk.PhotoImage(Image.open("/home/aditya/development/python/GUI/icons/linux.png"))
my_lable = Label(image=my_image)
my_lable.pack()

window.mainloop()