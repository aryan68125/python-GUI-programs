from tkinter import *
from tkinter import ttk
window = Tk()
window.title("full app scroll bar")

#inorder to add a scrollbar to our application 

#step 1 create a main frame which holds everything 
#.pack(fill=BOTH,expand=True) frame will fill the entire application window
main_frame = Frame(window).pack(fill=BOTH,expand=True)

#step 2 create a canvas
canvas = Canvas(main_frame)
canvas.pack(side=LEFT,fill=BOTH,expand=True)

#step 3 add a scrollbar to the canvas
#set the scrollbar to the main frame
#set the yScroll to the canvas and not to the main frame
Scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL,command = canvas.yview)
Scrollbar.pack(side=RIGHT,fill=Y)

#step 4 configure the canvas so that it has the scrollbar
canvas.configure(yscrollcommand = Scrollbar.set)
#now we need to bind this configure (Lambda e is the event)
canvas.bind("<Configure>", lambda e : canvas.configure(scrollregion = canvas.bbox("all")))

#step 5 then we are going to create another frame inside the canvas 
second_frame = Frame(canvas)

#step 6 then we will add that new frame to the window in our canvas
canvas.create_window((0,0),window=second_frame,anchor="nw")

#create 100 buttons 
for i in range(100):
    Button(second_frame, text=f"Button {i}").grid(row=i,column=0,padx=3,pady=5)

window.mainloop()