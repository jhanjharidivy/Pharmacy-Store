from tkinter import *
from tkinter.simpledialog import askstring

root = Tk()
root.geometry('100x100')


def check_password():
    pswd = askstring('PASSWORD', 'Enter Password', show='*')
    if pswd == "PASSWORD":
        open_admin()
    else:
        print('WRONG PASSWORD')


def open_admin():
    pass  # CODE FOR ADMIN WINDOW HERE


Button(root, text='OPEN ADMIN', command=check_password).pack()

root.mainloop()
