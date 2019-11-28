import cx_Oracle
from tkinter import *
from tkinter import messagebox


def search():
    try:
        # =============DB Connect======================#
        connstr = 'SOLVATIO/SOLVATIO@localhost'
        conn = cx_Oracle.connect(connstr)
        curs = conn.cursor()
        curs1 = conn.cursor()
        # =============first_query======================#
        curs.execute("select * from customers where afm='%s'" % afm.get())
        result = curs.fetchone()
        company_name.set(result[1])
        siebel_customer_code.set(result[3])
        # =============2nd_query======================#
        curs1.execute(
            "select name_project,description, count(*) from customer_desc where company_name_d='%s' group by name_project, description" % e2.get())
        results = curs1.fetchall()
        r_count = curs.rowcount
        if r_count == 0:
            print("no rows")
        else:
            for i in range(0, r_count):
                if i == 0:
                    name_project.set(results[0][0])
                    description.set(results[0][1])
                elif i == 1:
                    name_project.set(results[1][0])
                    description.set(results[1][1])
                elif i == 2:
                    name_project.set(results[2][0])
                    description.set(results[2][1])
                elif i == 3:
                    name_project.set(results[3][0])
                    description.set(results[3][1])
                else:
                    name_project.set(results[4][0])
                    description.set(results[4][1])

        e1.configure(state='disabled')
        conn.close()

    except:
        messagebox.showinfo('No data', 'No such data')


def clear():
    # ================Initialize==============#
    afm.set('')
    company_name.set('')
    siebel_customer_code.set('')
    name_project.set('')
    description.set('')
    e1.configure(state='normal')
    f1.configure(state='normal')


# ================GUI====================#
w1 = Tk()
w1.title('GUI Special Solutions')
w1.geometry('1350x750+0+0')
ptitle = Label(w1, font=('arial', 11, 'bold'), text='''Search Asset''')
ptitle.grid(row=0, column=0, columnspan=2)

# ========== Variables===================#
afm = StringVar()
company_name = StringVar()
siebel_customer_code = StringVar()
name_project = StringVar()
description = StringVar()

# ==========Buttons,TextBoxes ============#
l1 = Label(w1, text=' AFM ')
e1 = Entry(w1, textvariable=afm)
l2 = Label(w1, text=' Company ')
e2 = Entry(w1, textvariable=company_name)
l3 = Label(w1, text=' Siebel Code ')
e3 = Entry(w1, textvariable=siebel_customer_code)
b1 = Button(w1, text=' Search ', command=search)
b2 = Button(w1, text=' Clear ', command=clear)
l4 = Label(w1, text=' Project Name ')
f1 = Entry(w1, textvariable=name_project)
l5 = Label(w1, text=' Description ')
f2 = Entry(w1, textvariable=description, fg="lime green", bd=4, width=140)

f3 = Entry(w1, textvariable=name_project)
f4 = Entry(w1, textvariable=description, fg="lime green", bd=4, width=140)
f5 = Entry(w1, textvariable=name_project)
f6 = Entry(w1, textvariable=description, fg="lime green", bd=4, width=140)
f7 = Entry(w1, textvariable=name_project)
f8 = Entry(w1, textvariable=description, fg="lime green", bd=4, width=140)
f9 = Entry(w1, textvariable=name_project)
f10 = Entry(w1, textvariable=description, fg="lime green", bd=4, width=140)

l1.grid(row=1, column=0)
e1.grid(row=1, column=1)
l2.grid(row=2, column=0)
e2.grid(row=2, column=1)
l3.grid(row=3, column=0)
e3.grid(row=3, column=1)
b1.grid(row=1, column=2)
b2.grid(row=4, column=0)
l4.grid(row=5, column=0)
f1.grid(row=5, column=1)
l5.grid(row=5, column=2)
f2.grid(row=5, column=3)

f3.grid(row=6, column=1)
f4.grid(row=6, column=3)
f5.grid(row=7, column=1)
f6.grid(row=7, column=3)
f7.grid(row=8, column=1)
f8.grid(row=8, column=3)
f9.grid(row=9, column=1)
f10.grid(row=9, column=3)

w1.mainloop()