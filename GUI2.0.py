from tkinter import *

root = Tk()

def cal_funct():
    top = Toplevel(root)
    cal = Calendar(top, font = 'freesansbold', selectmode = 'day', year = 2019, month = 10, day = 7)
    cal.pack(fill = 'both', expand = 'True')

def date_funct():
    pass

button1 = Button(root, text = 'Calendar', command = cal_funct)
button2 = Button(root, text = 'Date Entry', command = date_funct)

button1.pack()
button2.pack()

mainloop()