from tkinter import *

root = Tk()
root.title('Converting temperature in Celsius to Fahrenheit')

#Adding the basic widgets and placing them in the proper order
l1 = Label(root, text = 'Temperature (in C): ')
l2 = Label(root, text = 'Temperature (in F): ')
 
e1 = Entry(root, width = 10, borderwidth = 3)
e2 = Entry(root, width = 10, borderwidth = 3)

#Defining a function
def temp_convert():
    if len(str(e1.get())) > 0:
        tmp_f = ((9/5) * float(e1.get())) + 32
        e2.delete(0, END)
        e2.insert(0, tmp_f)
    
    elif len(str(e2.get())) > 0:
        tmp_c = (5/9) * (float(e2.get()) - 32)
        e1.delete(0, END)
        e1.insert(0, tmp_c)
    
def clear():
    e1.delete(0, END)
    e2.delete(0, END)

b1 = Button(root, text = 'Convert', padx = 5, pady = 5, command = temp_convert)
b2 = Button(root, text = 'Clear', padx = 5, pady = 5, command = clear)    
    
#Placing them on the grid
l1.grid(row = 0, column = 0)
l2.grid(row = 1, column = 0)
e1.grid(row = 0, column = 1, padx = 5, pady = 5)
e2.grid(row = 1, column = 1, padx = 5, pady = 5)
b1.grid(row = 2, column = 1)
b2.grid(row = 2, column = 0)

root.mainloop()