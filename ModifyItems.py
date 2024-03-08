from tkinter import *
import tkinter.messagebox
import mysql.connector as connector
import pandas

#******************* Method For Displaying Modify Items Form ***********************

def modifyitem():
    def updateitemdata():
        mydb = connector.connect(host="localhost", user="root", passwd="hardikjain", database="Restaurant")
        mycursor = mydb.cursor()
        itemno = txtitemno.get()
        itemname = txtitemname.get()
        itemrate = txtitemrate.get()
        qry = "update itemsmaster set itemname='{}', rate={} where itemno= {}".format(itemname, itemrate, itemno)
        mycursor.execute(qry)
        mydb.commit()
        mainwindow.destroy()
        tkinter.messagebox.showinfo('Information', 'Updated !')

    def showselecteditem():
        mydb = connector.connect(host="localhost", user="root", passwd="hardikjain", database="Restaurant")
        mycursor = mydb.cursor()
        itemno = txtitemno.get()
        qry = "select itemname,rate from itemsmaster where itemno = {}".format(itemno)
        mycursor.execute(qry)
        data = pandas.DataFrame(mycursor.fetchall(),columns=['itemname','rate'])

        nm = str(data.at[0,'itemname'])
        rate = str(data.at[0,'rate'])
        txtitemname.insert(0,nm)
        txtitemrate.insert(0,rate)




    mainwindow = Tk()
    mainwindow.geometry('800x600')

    headinglabel = Label(mainwindow, text="Modify Item Form", font='times 24 bold underline')
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

    updatebutton = Button(mainwindow, text='Update Items', width=30, command = updateitemdata)
    updatebutton.place(x=50, y=305)

    searchbutton = Button(mainwindow, text='Search Item', width=30, command = showselecteditem)
    searchbutton.place(x=400,y=155)

    txtitemno.focus()
    mainwindow.mainloop()

