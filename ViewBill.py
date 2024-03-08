from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector as connector
import pandas


def showsavedbillform():

    def showinfo():
        mydb = connector.connect(host="localhost", user="root", passwd="root", database="Restaurant")
        mycursor = mydb.cursor()
        mycursor.execute(f"Select * from bill where billno = {txtbillno.get()}")
        result = mycursor.fetchall()
        DF = pandas.DataFrame(result, columns=['billno', 'billdate', 'name','description','grandtotal'])
        print(list(DF['description']))
        txtdata.insert(END, list(DF['description'])[0])
        txtdata.config(state='disabled')
        txtgrandtotal.insert(0,list(DF['grandtotal']))
        txtname.insert(0,list(DF['name']))
        txtbilldate.insert(0,list(DF['billdate']))

    # ****************************************** Window Layout ****************************************
    mainwindow = Tk()
    mainwindow.geometry('800x640')

    headinglabel = Label(mainwindow, text="View Saved Bill", font='times 24 bold underline')
    itemlabel = Label(mainwindow, text="Enter Bill No To Show", font='times 12 bold')
    txtbillno = Entry(mainwindow)

    txtdata = Text(mainwindow, width=70, height=12)
    grandtotallabel = Label(mainwindow, text="Grand Total", font='times 12 bold')
    txtgrandtotal = Entry(mainwindow)
    billdatelabel = Label(mainwindow, text="Bill Date", font='times 12 bold')
    txtbilldate = Entry(mainwindow)
    namelabel = Label(mainwindow, text="Name Of Person", font='times 12 bold')
    txtname= Entry(mainwindow,width=50)
    btnshowbillinfo = Button(mainwindow, text='Show', width=15, font='times 10 bold', command = showinfo)

    headinglabel.place(x=300, y=15)
    itemlabel.place(x=50, y=80)
    txtbillno.place(x=220,y=80)
    btnshowbillinfo.place(x = 400,y=80)
    txtdata.place(x=50, y=200)
    grandtotallabel.place(x=50, y=480)
    txtgrandtotal.place(x=150, y=485)
    billdatelabel.place(x=400, y=485)
    txtbilldate.place(x = 480, y=485)
    namelabel.place(x=50,y=520)
    txtname.place(x=200,y = 525)

    mainwindow.mainloop()
