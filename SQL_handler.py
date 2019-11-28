from tkinter import *
from tkinter import filedialog
import sqlite3
import csv


# key press functions
#EXECUTE key press
def execute():
    entered_text = entry.get('1.0', 'end-1c')  # collect text from the text entry box
    entry.delete('1.0', 'end-1c')  # and clear the entry box!
    try:
        display.insert(END, entered_text + '\n')
        display.see(END)
        cursor.execute(entered_text)
        db.commit()
        output_text = cursor.fetchall()
    except Exception as e:
        output_text = "ERROR: " + str(e)
    if output_text != []:
        display.insert(END, output_text)
    display.insert(END, '\n>')


#RUN A SCRIPT key press
def script(filename):
    fd = open(filename, 'r')
    sqlFile = fd.read()

    sqlCommands = sqlFile.split(";")

    for command in sqlCommands:
        try:
            c.execute(command)
        except OperationalError:
            print("Command skipped")
    fd.close()
    # find out the file name

    # read it

    # parse for each command in turn (blank lines indicate this)
    # put that command into 'entry' with an entry.insert
  # entry.insert()
    # and 'execute' it
  # entry.delete('end-3c', END)
  # entry.insert(END, ';')
    # check for EOF, and repeat


#BULK DATA key press
def datafill():
    filename = filedialog.askopenfilename(title="Choose a .csv file")
    window.update()
    # replace the next line to get the table name via a widget, rather than 'input' ...
    tablename = input("What is the (case sensitive) TABLE name for this data?")
    window.attributes("-topmost", True)
    window.focus_force()
    with open(filename, newline='') as thefile:
        data = csv.reader(thefile)
        fieldnames = thefile.readline()
        entry.insert(END, "INSERT INTO " + tablename + " (" + fieldnames[0:-1] + ")\nVALUES\n")
        entry.see(END)
        for row in data:
            massage = str(row)
            entry.insert(END, "\t(" + massage[1:-1] + "),\n")
            entry.see(END)
        entry.delete('end-3c', END)
        entry.insert(END, ';')
        execute()


#CLEAR I/P key press
def clearip():
    entry.delete('1.0', 'end-1c')


#CLEAR Q/P key press
def clearop():
    display.delete('1.0', 'end-1c')


def dummy():
    pass


##### main
window = Tk()
window.title("SQL Utility")

# create the instructions 'label'
Label(window, text="SQL command: ").grid(row=0, column=0, sticky=W + N)
Label(window, text="Response: ").grid(row=3, column=0, sticky=E + N)

# create a text box for input
entry = Text(window, width=105, height=6, wrap=WORD, background="light grey")
entry.grid(row=0, column=1, columnspan=4, sticky=W)

# create a frame for the buttons
buttons = Frame()
buttons.grid(row=2, column=1, sticky=W)

# and put the buttons in it (creates buttons for functions
Button(buttons, text="EXECUTE", width=7, command=execute).grid(row=0, column=1, sticky=W)
Button(buttons, text="RUN A SCRIPT", width=12, command=script).grid(row=0, column=2, sticky=W)
Button(buttons, text="BULK DATA", width=9, command=datafill).grid(row=0, column=3, sticky=W)
Button(buttons, text="     ", width=5, command=dummy).grid(row=0, column=4, sticky=W)
Button(buttons, text="CLEAR INPUT", width=11, command=clearip).grid(row=0, column=5, sticky=W)
Button(buttons, text="CLEAR OUTPUT", width=12, command=clearop).grid(row=0, column=6, sticky=W)

# create a text box for output
display = Text(window, width=105, height=12, wrap=WORD, background="light blue")
display.grid(row=3, column=1, columnspan=8, sticky=W)

# run mainloop
with sqlite3.connect("starter.db") as db:
    cursor = db.cursor()

window.mainloop()