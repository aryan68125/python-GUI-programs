import tkinter as Tk

master = Tk.Tk()

listbox = Tk.Listbox(master)
listbox.pack()

# Insert few elements in listbox:
for item in [1, 2, 3, "three", "four", "five", "six", "seven"]:
    listbox.insert(Tk.END, item)
    print
# Return index of desired element to seek for
def check_index(element):
   try:
       index = listbox.get(0, "end").index(element)
       return index
   except ValueError:
       print('Item can not be found in the list!')
       index = -1 # Or whatever value you want to assign to it by default
       return index

print (check_index('three'))    # Will print 3

print (check_index(1)) # This will print:
                     # Item can not be found in the list!
                     # -1

Tk.mainloop()