from tkinter import *

root = Tk()

frame = LabelFrame(root, padx = 15, pady = 15)
frame.pack(padx = 10, pady = 10)

my_menu = Menu(root)
root.config(menu = my_menu)

def out():
    pass

#Create menu item

file_menu = Menu(my_menu)
my_menu.add_cascade(label = 'File' , menu = file_menu)

file_menu.add_command(label = 'New..', command = out)
file_menu.add_command(label = 'Exit', command = root.quit)

root.mainloop()