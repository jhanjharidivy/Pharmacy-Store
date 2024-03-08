import tkinter as tk
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter.simpledialog import askstring
import mysql.connector as conn
from pandas import DataFrame
import time

database = conn.connect(host="localhost", user="root", passwd="root", database="medshop")
cursor = database.cursor()
totalprice = 0
cursor.execute("select sp from sales;")
data = cursor.fetchall()
sd = list()
for i in range(len(data)):
    sd.append(data[i][0])
prices = {'Gelusil': sd[0], 'Combiflam': sd[1], 'Amocixillin': sd[2], 'Xanax': sd[3], 'Allegra': sd[4]}


def main_window():
    root = tk.Tk()
    root.title('MEDICAL STORE')

    # --------------------------------------------------------------------------------------------------------------SHOP
    def shop_medicines():
        global totalprice, prices
        shopwin = tk.Toplevel(root)
        shopwin.geometry("600x500+100+100")
        shopwin.title('Shop for Medicines')
        shopwin.resizable(False, False)
        shopwin.focus_set()

        templabel = Label(shopwin, text='LOADING SHOP...', font='Courier 20')
        templabel.place(x=175, y=200)
        root.update()
        time.sleep(1)
        templabel.place_forget()

        Label(shopwin, text='Choose Category', font='times 25').pack()
        Label(shopwin).pack()

        Style().configure('lefttab.TNotebook', tabposition='wn')
        Style().configure('TNotebook.Tab', font='Courier 12', padding=[0, 10])

        shopCategoryBook = Notebook(shopwin, style="lefttab.TNotebook")

        antacidFrame = tk.Frame(shopCategoryBook, height=300, width=500)
        painkillerFrame = tk.Frame(shopCategoryBook, height=300, width=500)
        antibioticFrame = tk.Frame(shopCategoryBook, height=300, width=500)
        depressantFrame = tk.Frame(shopCategoryBook, height=300, width=500)
        antiallergyFrame = tk.Frame(shopCategoryBook, height=300, width=500)

        values_spin = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        pricevar = tk.IntVar()
        pricevar.set(totalprice)
        Label(shopwin, text='Total :', font='Courier 14').place(x=100, y=370)
        Label(shopwin, textvariable=pricevar, font='Courier 14').place(x=200, y=370)

        def calcprice():
            global totalprice
            totalprice += int(qtyGelusil.get()) * prices['Gelusil']
            totalprice += int(qtyCombiflam.get()) * prices['Combiflam']
            totalprice += int(qtyAmocixillin.get()) * prices['Amocixillin']
            totalprice += int(qtyXanax.get()) * prices['Xanax']
            totalprice += int(qtyAllegra.get()) * prices['Allegra']

        def change_prices():
            global totalprice
            calcprice()
            pricevar.set(totalprice)
            totalprice = 0

        # -------------------------------------------------------------------------------------------------Antacid Frame
        Label(antacidFrame, text='=> Gelusil', font='times 20').place(x=10, y=20)
        Label(antacidFrame, text='A sample antacid', font='Courier 13').place(x=70, y=60)
        Label(antacidFrame, text='Quantity :', font='Courier 13').place(x=70, y=90)
        qtyGelusil = tk.Spinbox(antacidFrame, values=values_spin, font="Courier 12", width=5, command=change_prices)
        qtyGelusil.place(x=190, y=90)

        # ----------------------------------------------------------------------------------------------Painkiller Frame
        Label(painkillerFrame, text='=> Combiflam', font='times 20').place(x=10, y=20)
        Label(painkillerFrame, text='A sample painkiller', font='Courier 13').place(x=70, y=60)
        Label(painkillerFrame, text='Quantity :', font='Courier 13').place(x=70, y=90)
        qtyCombiflam = tk.Spinbox(painkillerFrame, values=values_spin, font="Courier 12", width=5, command=change_prices)
        qtyCombiflam.place(x=190, y=90)

        # ----------------------------------------------------------------------------------------------Antibiotic Frame
        Label(antibioticFrame, text='=> Amocixillin', font='times 20').place(x=10, y=20)
        Label(antibioticFrame, text='A sample antibiotic', font='Courier 13').place(x=70, y=60)
        Label(antibioticFrame, text='Quantity :', font='Courier 13').place(x=70, y=90)
        qtyAmocixillin = tk.Spinbox(antibioticFrame, values=values_spin,
                                    font="Courier 12", width=5, command=change_prices)
        qtyAmocixillin.place(x=190, y=90)

        # ----------------------------------------------------------------------------------------------Depressant Frame
        Label(depressantFrame, text='=> Xanax', font='times 20').place(x=10, y=20)
        Label(depressantFrame, text='A sample depressant', font='Courier 13').place(x=70, y=60)
        Label(depressantFrame, text='Quantity :', font='Courier 13').place(x=70, y=90)
        qtyXanax = tk.Spinbox(depressantFrame, values=values_spin, font="Courier 12", width=5, command=change_prices)
        qtyXanax.place(x=190, y=90)

        # ---------------------------------------------------------------------------------------------AntiAllergy Frame
        Label(antiallergyFrame, text='=> Allegra', font='times 20').place(x=10, y=20)
        Label(antiallergyFrame, text='A sample antiallergy drug', font='Courier 13').place(x=70, y=60)
        Label(antiallergyFrame, text='Quantity :', font='Courier 13').place(x=70, y=90)
        qtyAllegra = tk.Spinbox(antiallergyFrame, values=values_spin, font="Courier 12", width=5, command=change_prices)
        qtyAllegra.place(x=190, y=90)

        shopCategoryBook.add(antacidFrame, text='Antacids   ')
        shopCategoryBook.add(painkillerFrame, text='PainKillers')
        shopCategoryBook.add(antibioticFrame, text='Antibiotics')
        shopCategoryBook.add(depressantFrame, text='Depressants')
        shopCategoryBook.add(antiallergyFrame, text='AntiAllergy')
        shopCategoryBook.pack()

        def complete_purchase():
            global totalprice
            gelusil = int(qtyGelusil.get())
            combiflam = int(qtyCombiflam.get())
            amocixillin = int(qtyAmocixillin.get())
            xanax = int(qtyXanax.get())
            allegra = int(qtyAllegra.get())

            cursor.execute('select stock from sales order by itemno;')
            rawstock = cursor.fetchall()
            stocks_left = list()
            for o in range(len(data)):
                stocks_left.append(rawstock[o][0])
            if stocks_left[0] - gelusil >= 0 and stocks_left[1] - combiflam >= 0 and stocks_left[2] - amocixillin >= 0:
                if stocks_left[3] - xanax >= 0 and stocks_left[4] - allegra >= 0:
                    itemsqty = gelusil + combiflam + amocixillin + xanax + allegra
                    if itemsqty != 0:
                        list_items = {'Gelusil': gelusil, 'Combiflam': combiflam, 'Amocixillin': amocixillin,
                                      'Xanax': xanax, 'Allegra': allegra}
                        strshow = 'Purchased Items\n'
                        for q in list_items:
                            if list_items[q] != 0:
                                strshow += q + ' : ' + str(list_items[q]) + '\n'
                        calcprice()
                        strshow += '\nTotal Price : ' + str(totalprice)
                        confirm_order = askyesno('CONFIRM', strshow, parent=shopwin)
                        if confirm_order:
                            cursor.execute("insert into bill(billdate, gelusil, combiflam, amocixillin, xanax,"
                                           f" allegra, total) values(curdate(), {gelusil}, {combiflam}, {amocixillin},"
                                           f" {xanax}, {allegra}, {totalprice});")
                            database.commit()
                            cursor.execute(f"update sales set stock={stocks_left[0] - gelusil} where itemno=1;")
                            cursor.execute(f"update sales set stock={stocks_left[1] - combiflam} where itemno=2;")
                            cursor.execute(f"update sales set stock={stocks_left[2] - amocixillin} where itemno=3;")
                            cursor.execute(f"update sales set stock={stocks_left[3] - xanax} where itemno=4;")
                            cursor.execute(f"update sales set stock={stocks_left[4] - allegra} where itemno=5;")
                            database.commit()
                            cursor.execute(f"update profit set sales=sales+{totalprice};")
                            database.commit()
                            showinfo('SUCCESS', 'Items purchased !', parent=shopwin)
                            shopwin.destroy()
                            totalprice = 0
                        else:
                            showwarning('CANCEL', 'Purchase Cancelled by user', parent=shopwin)
                            totalprice = 0
                    else:
                        showerror("QuantityError", 'Please select an item to continue', parent=shopwin)
            else:
                showinfo('OUT OF STOCK !', 'The medicines you want to purchase are out of stock !\nCheck back later !')

        def enter_p(event):
            purchaseBtn['bg'] = "lightpink"
            purchaseBtn['fg'] = "white"

        def leave_p(event):
            purchaseBtn['bg'] = "#F0F0F0"
            purchaseBtn['fg'] = "black"

        purchaseBtn = tk.Button(shopwin, text='Purchase', font='Courier 17', relief=tk.SOLID, command=complete_purchase)
        purchaseBtn.bind("<Enter>", enter_p)
        purchaseBtn.bind("<Leave>", leave_p)
        purchaseBtn.place(x=250, y=400)

        shopwin.mainloop()

    # ---------------------------------------------------------------------------------------------------------SHOW_BILL
    def check_not_empty():
        cursor.execute('select * from bill;')
        trashlist = cursor.fetchall()
        if len(trashlist) == 0:
            showwarning('BLANK', 'Purchase something to show bills !')
        else:
            show_bills()

    def show_bills():
        def change_bills(event):
            newbill = billDisplayBox.get(tk.ACTIVE)
            if newbill[len(newbill) - 3:].isdigit():
                newbillno = newbill[len(newbill) - 3:]
            elif newbill[len(newbill) - 2:].isdigit():
                newbillno = newbill[len(newbill) - 2:]
            else:
                newbillno = newbill[-1]
            billnovar.set(newbillno)
            cursor.execute(f'select * from bill where billno={newbillno}')
            info = cursor.fetchall()[0]
            billdatevar.set(info[1])
            gelusilvar.set(info[2])
            combiflamvar.set(info[3])
            amocixillinvar.set(info[4])
            xanaxvar.set(info[5])
            allegravar.set(info[6])
            totalvar.set(info[7])

        billwin = tk.Toplevel(root)
        billwin.geometry('600x500+100+100')
        billwin.title('Display Bills')
        billwin.resizable(False, False)
        billwin.focus_set()

        Label(billwin, font='Courier 14', text='Bill Numbers').pack(anchor=tk.NW)
        billDisplayBox = tk.Listbox(billwin, height=24, width=17, font='Courier 14', selectmode=tk.BROWSE)
        billDisplayBox.pack(anchor=tk.NW, side=tk.LEFT)
        billDisplayscrollbar = tk.Scrollbar(billwin, orient=tk.VERTICAL)
        billDisplayscrollbar.pack(anchor=tk.NW, side=tk.LEFT, fill=tk.Y)
        billDisplayscrollbar.config(command=billDisplayBox.yview)
        billDisplayBox.config(yscrollcommand=billDisplayscrollbar.set)

        billDisplayBox.bind('<Return>', change_bills)
        billDisplayBox.bind('<Button-1>', change_bills)

        billnovar = tk.IntVar()
        billdatevar = tk.StringVar()
        gelusilvar = tk.IntVar()
        combiflamvar = tk.IntVar()
        amocixillinvar = tk.IntVar()
        xanaxvar = tk.IntVar()
        allegravar = tk.IntVar()
        totalvar = tk.IntVar()

        cursor.execute('select billno from bill;')
        rawlist = list(cursor.fetchall())
        list_billno = list()
        for i in range(len(rawlist)):
            list_billno.append(rawlist[i][0])

        for i in list_billno:
            billDisplayBox.insert(tk.END, 'Bill No. ' + str(i))

        tk.Button(billwin, height=30, width=40, relief=tk.SOLID, borderwidth=5, state=tk.DISABLED).place(x=250, y=25)

        Label(billwin, text='BILL', font='Algerian 20 underline').place(x=375, y=50)
        Label(billwin, text='Bill Number :', font='Courier 13').place(x=300, y=100)
        Label(billwin, textvariable=billnovar, font='Courier 13').place(x=440, y=100)
        Label(billwin, text='Bill Date :', font='Courier 13').place(x=300, y=150)
        Label(billwin, textvariable=billdatevar, font='Courier 13').place(x=420, y=150)
        Label(billwin, text='Gelusil Qty :', font='Courier 13').place(x=300, y=200)
        Label(billwin, textvariable=gelusilvar, font='Courier 13').place(x=440, y=200)
        Label(billwin, text='Combiflam Qty :', font='Courier 13').place(x=300, y=230)
        Label(billwin, textvariable=combiflamvar, font='Courier 13').place(x=460, y=230)
        Label(billwin, text='Amocixillin Qty :', font='Courier 13').place(x=300, y=260)
        Label(billwin, textvariable=amocixillinvar, font='Courier 13').place(x=480, y=260)
        Label(billwin, text='Xanax Qty :', font='Courier 13').place(x=300, y=290)
        Label(billwin, textvariable=xanaxvar, font='Courier 13').place(x=420, y=290)
        Label(billwin, text='Allegra Qty :', font='Courier 13').place(x=300, y=320)
        Label(billwin, textvariable=allegravar, font='Courier 13').place(x=440, y=320)
        Label(billwin, text='-' * 20, font='Courier 13').place(x=300, y=380)
        Label(billwin, text='Total Cost :', font='Courier 13').place(x=300, y=410)
        Label(billwin, textvariable=totalvar, font='Courier 13').place(x=440, y=410)
        Label(billwin, text='-' * 20, font='Courier 13').place(x=300, y=440)

        billwin.mainloop()

    # -------------------------------------------------------------------------------------------------------------ADMIN
    def admin_section():
        global prices
        password = askstring('ADMIN', 'Enter Password to access admin section', show='*')
        if str(password).lower() == 'admin':
            adminwin = tk.Toplevel(root)
            adminwin.geometry("600x500+100+100")
            adminwin.title('Admin Section')
            adminwin.resizable(False, False)
            adminwin.focus_set()

            Label(adminwin, text='Current Stocks', font='Courier 15 underline').pack()

            cursor.execute('select stock from sales order by itemno;')
            rawstock = cursor.fetchall()
            stocks_left = list()
            for o in range(len(rawstock)):
                stocks_left.append(rawstock[o][0])

            gelusilvar = tk.IntVar()
            gelusilvar.set(stocks_left[0])
            combiflamvar = tk.IntVar()
            combiflamvar.set(stocks_left[1])
            amocixillinvar = tk.IntVar()
            amocixillinvar.set(stocks_left[2])
            xanaxvar = tk.IntVar()
            xanaxvar.set(stocks_left[3])
            allegravar = tk.IntVar()
            allegravar.set(stocks_left[4])

            cursor.execute('select * from profit;')
            profit_data = cursor.fetchall()[0]
            purchasesvar = tk.IntVar()
            purchasesvar.set(profit_data[0])
            salesvar = tk.IntVar()
            salesvar.set(profit_data[1])

            def add_stocks():
                addstockwin = tk.Toplevel(root)
                addstockwin.title('ADD STOCKS')
                addstockwin.geometry('300x300+350+200')
                addstockwin.resizable(False, False)
                addstockwin.focus_set()

                def on_select(event):
                    addstockwin.focus_set()

                def on_add():
                    medicine = medcombo.get()
                    if str(entryqty.get()).isdigit() and medicine in list(prices.keys()):
                        finalresp = askyesno('CONFIRM', f'Are you sure you want to'
                                                        f' purchase {entryqty.get()} {medicine} ?', parent=addstockwin)
                        if finalresp:
                            cursor.execute(f"select cp from sales where itemname='{medicine.lower()}';")
                            cp = cursor.fetchone()[0]
                            price = cp * int(entryqty.get())
                            cursor.execute(f"update profit set purchases=purchases+{price};")
                            database.commit()
                            cursor.execute(f"update sales set stock=stock+{int(entryqty.get())}"
                                           f" where itemname='{medicine.lower()}';")
                            database.commit()
                            purchasesvar.set(purchasesvar.get() + price)
                            if medicine.lower() == 'gelusil':
                                gelusilvar.set(gelusilvar.get() + int(entryqty.get()))
                            elif medicine.lower() == 'combiflam':
                                combiflamvar.set(combiflamvar.get() + int(entryqty.get()))
                            elif medicine.lower() == 'amocixillin':
                                amocixillinvar.set(amocixillinvar.get() + int(entryqty.get()))
                            elif medicine.lower() == 'xanax':
                                xanaxvar.set(xanaxvar.get() + int(entryqty.get()))
                            elif medicine.lower() == 'allegra':
                                allegravar.set(allegravar.get() + int(entryqty.get()))
                            showinfo('SUCCESS', f'Successfully purchased {entryqty.get()} {medicine} for Rs. {price}!',
                                     parent=addstockwin)
                            addstockwin.destroy()
                        else:
                            showwarning('InterruptError', 'Purchase cancelled by user!', parent=addstockwin)
                    else:
                        showerror('ERROR', 'Wrong entries or blank entries !', parent=addstockwin)

                Label(addstockwin, text='Add Stocks', font='Courier 15 underline').pack()
                Label(addstockwin, text='Medicine :', font='Courier 12').pack(anchor=tk.NW)
                medcombo = Combobox(addstockwin, font='Courier 10', values=list(prices.keys()))
                medcombo.bind("<<ComboboxSelected>>", on_select)
                medcombo.place(x=10, y=60)
                Label(addstockwin, text='Quantity :', font='Courier 12').place(x=0, y=100)
                entryqty = Entry(addstockwin, font='Courier 10')
                entryqty.place(x=10, y=130)
                tk.Button(addstockwin, text='PURCHASE', font='Courier 15',
                          command=on_add, relief=tk.SOLID).place(x=80, y=200)

                addstockwin.mainloop()

            def price_and_profit():
                ppwin = tk.Toplevel(root)
                ppwin.title('Price & Profit')
                ppwin.resizable(False, False)
                ppwin.geometry('+300+100')
                ppwin.focus_set()

                cursor.execute('select cp, sp from sales;')
                raw = cursor.fetchall()
                pptext = tk.Text(ppwin, height=7, width=30, font='Courier 14')
                pptext.pack()
                cplist = list()
                splist= list()
                for c in raw:
                    cplist.append(c[0])
                    splist.append(c[1])
                profitlist = list()
                for v in range(5):
                    profitlist.append(splist[v] - cplist[v])
                dict_pp = {'Name': list(prices.keys()), 'Cp': cplist, 'Sp': splist, 'Profit': profitlist}
                df_pp = DataFrame(dict_pp)
                pptext.insert("1.0", df_pp)
                pptext['state'] = tk.DISABLED

                ppwin.mainloop()

            Label(adminwin, text='Gelusil :', font='Courier 13').place(x=10, y=30)
            Label(adminwin, textvariable=gelusilvar, font='Courier 13').place(x=110, y=30)
            Label(adminwin, text='Combiflam :', font='Courier 13').place(x=10, y=60)
            Label(adminwin, textvariable=combiflamvar, font='Courier 13').place(x=130, y=60)
            Label(adminwin, text='Amocixillin :', font='Courier 13').place(x=10, y=90)
            Label(adminwin, textvariable=amocixillinvar, font='Courier 13').place(x=150, y=90)
            Label(adminwin, text='Xanax :', font='Courier 13').place(x=10, y=120)
            Label(adminwin, textvariable=xanaxvar, font='Courier 13').place(x=100, y=120)
            Label(adminwin, text='Allegra :', font='Courier 13').place(x=10, y=150)
            Label(adminwin, textvariable=allegravar, font='Courier 13').place(x=110, y=150)

            Label(adminwin, text='PURCHASES : Rs', font='Courier 18').place(x=250, y=50)
            Label(adminwin, textvariable=purchasesvar, font='Courier 18').place(x=460, y=50)
            Label(adminwin, text='SALES : Rs', font='Courier 18').place(x=250, y=125)
            Label(adminwin, textvariable=salesvar, font='Courier 18').place(x=400, y=125)

            tk.Button(adminwin, text='Add Stocks', width=25, relief=tk.SOLID,
                      font='times 20 bold', command=add_stocks).place(x=100, y=200)

            tk.Button(adminwin, text='Price & Profit', width=25, relief=tk.SOLID,
                      font='times 20 bold', command=price_and_profit).place(x=100, y=275)

            adminwin.mainloop()
        else:
            if password is None:
                pass
            else:
                showerror('ERROR', 'Wrong Admin password\nACCESS DENIED')

    # --------------------------------------------------------------------------------------------------------------MAIN
    Label(root, text="<NAME> Medical Store", font='times 24 bold underline').place(x=220, y=20)

    tk.Button(root, text='Shop for Medicines', width=25, relief=tk.SOLID,
              font='times 20 bold', command=shop_medicines).place(x=200, y=100)

    tk.Button(root, text='Display Previous Bills', width=25, relief=tk.SOLID,
              font='times 20 bold', command=check_not_empty).place(x=200, y=200)

    tk.Button(root, text='Shop Owner Section', width=25, relief=tk.SOLID,
              font='times 20 bold', command=admin_section).place(x=200, y=300)

    width = 800
    height = 700
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()

    # Make it center screen
    x = str(int(screenwidth / 2 - width / 2))
    y = str(int(screenheight / 2 - height / 2))
    s = '800x600+' + x + '+' + y
    root.geometry(s)
    root.resizable(False, False)
    root.mainloop()


main_window()
