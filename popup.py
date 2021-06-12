#this program shows you how to use pop up window in our application
from tkinter import *
from PIL import ImageTk,Image
#import message box to create a pop up window of information display type
from tkinter import messagebox

window = Tk()
window.title("how to create a pop up window")

def popup():
    #create a message box showinfo will just show some kind of information on the pop up window it is not interactive
    #showinfo("the title bar that you want to show up", message that you want to show in your actual pop up window)
    messagebox.showwarning("developer info", "Name = Aditya Kumar \n class = B.tech 2nd year \n college = SITM")

#this function shows how you can write logic for handeling yes or no button of the popup window
def popupAskYesNo():
    #create a message box showinfo will just show some kind of information on the pop up window it is not interactive
    #showinfo("the title bar that you want to show up", message that you want to show in your actual pop up window)
    delete_response = messagebox.askyesno("warnimg", "Do you want to delete this file?")
    if delete_response==1:
        my_lable=Label(window,text="Yes Delete the file")
        my_lable.grid(row=3,column=0,pady=10)
    else:
        my_lable=Label(window,text="No keep the file")
        my_lable.grid(row=3,column=0,pady=10)

    
#there are different type of popup windows present in python tkinter library
#showinfo , showwarning, showerror,askquestion,askokcancel,askyesno

info = Button(window,text="dev info",command = popup)
info.grid(row=1,column=0,pady=10)

delete = Button(window,text = "delete!",command = popupAskYesNo)
delete.grid(row=2,column=0,pady=10)

window.mainloop()