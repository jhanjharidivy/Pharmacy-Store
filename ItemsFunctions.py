from tkinter import *
import tkinter.messagebox
import mysql.connector as connector
import pandas

#******************* Method For Displaying Create Items Form ***********************

def createitemform():
    def insertnewitemdata():
        mydb = connector.connect(host="localhost", user="root", passwd="root", database="Restaurant")
        mycursor = mydb.cursor()

        itemno = txtitemno.get()
        itemname = txtitemname.get()
        itemrate = txtitemrate.get()
        qry = "insert into itemsmaster values({},'{}',{})".format(itemno, itemname,itemrate)
        mycursor.execute(qry)
        mydb.commit()
        mainwindow.destroy()
        tkinter.messagebox.showinfo('Information', 'Item Created successfully !')


    mainwindow = Tk()
    mainwindow.geometry('800x500')

    headinglabel = Label(mainwindow, text="Item Creation form", font='times 24 bold underline')
    headinglabel.place(x=280, y=20)

    lblitemno = Label(mainwindow, text='Enter Item Number', font='times 15')
    lblitemname = Label(mainwindow, text='Enter Item Name', font='times 15')
    lblitemrate = Label(mainwindow, text='Enter Charges', font='times 15')

    txtitemno = Entry(mainwindow)
    txtitemname = Entry(mainwindow)
    txtitemrate = Entry(mainwindow)

    lblitemno.place(x=50, y=150)
    lblitemname.place(x=50, y=200)
    lblitemrate.place(x=50, y=250)

    txtitemno.place(x=250, y=155)
    txtitemname.place(x=250, y=205)
    txtitemrate.place(x=250, y=255)

    savebutton = Button(mainwindow, text='Save Item', width=30, command=insertnewitemdata)
    savebutton.place(x=50, y=305)

    txtitemno.focus()
    mainwindow.mainloop()

# ******************Method For Showing All Items Form*******************************

def showallitems():
    def loaddata():
        mydb = connector.connect(host="localhost", user="root", passwd="root", database="Restaurant")
        mycursor = mydb.cursor()
        mycursor.execute('Select * from itemsmaster')
        result = mycursor.fetchall()
        DF = pandas.DataFrame(result, columns=['ItemNO', 'ItemName', 'Rate'])
        txtdata.insert(INSERT, DF)
        txtdata.config(state='disabled')

    mainwindow = Tk()
    mainwindow.geometry('800x400')
    headinglabel = Label(mainwindow, text="All Items Information", font='times 24 bold underline')
    headinglabel.place(x=250, y=20)
    txtdata = Text(mainwindow, width=70, height=12)
    txtdata.place(x=50, y=100)
    loadbutton = Button(mainwindow, text='Load Data', width=20, command=loaddata, font='times 15 bold')
    loadbutton.place(x=50, y=305)
    mainwindow.mainloop()
