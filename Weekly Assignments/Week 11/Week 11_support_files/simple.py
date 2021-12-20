from tkinter import *

window = Tk()

def km_miles():
    miles = float(e1_val.get()) * 1.6
    t1.delete("1.0", END)
    t1.insert(END, miles)
    print('Successfully converted')
    
l1 = Label(window, text='Enter kilometers: ')
l1.grid(row = 0, column = 0)

e1_val = StringVar()
e1 = Entry(window, textvariable = e1_val)
e1.grid(row=0, column=1)

l2 = Label(window, text='Miles converted: ')
l2.grid(row=1, column=0)

t1 = Text(window, height=1, width = 20)
t1.grid(row=1, column=1)

b = Button(window, text='Convert', command = km_miles)
b.grid(row=2, column=1)

window.mainloop()