import time
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
from prettytable import PrettyTable
import sqlite3

root = tk.Tk()
root.title('H A L O')

windowWidth = 700
windowHeight = 330
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
xCordinate = int((screenWidth/2) - (windowWidth/2))
yCordinate = int((screenHeight/2) - (windowHeight/2))
root.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, xCordinate, yCordinate))
email_var = tk.StringVar()
pass_var = tk.StringVar()
addApp_var = tk.StringVar()
addAccount_var = tk.StringVar()
addPassword_var = tk.StringVar()

photo = PhotoImage(file ="../ComputerCPT/HaloLogo.gif")
panel = Label(root, image = photo)
panel.place(x=490,y=0)
def picture():
    photo = PhotoImage(file="../ComputerCPT/HaloLogo.gif")
    panel = Label(root, image=photo)
    panel.place(x=490, y=0)


style = ttk.Style(root)

root.tk.call('source', 'azure-dark.tcl')

style.theme_use('azure-dark')

checkframe = ttk.LabelFrame(root, text='Login', width=460, height=300)
checkframe.place(x=20, y=12)

def clear_frame():
   for widgets in root.winfo_children():
      widgets.destroy()
def storage():
    root.destroy()
    import main

def check():
    while email_var.get() == "" and pass_var.get() == "":
        return messagebox.showinfo("Login", "Invalid Fields.")

    with sqlite3.connect(
            'HaloSystem.db') as db:
        cursor = db.cursor()

    cursor.execute("SELECT 1 FROM users WHERE username = ? AND password = ?", (email_var.get(), pass_var.get()))
    while len(cursor.fetchall()) == 0:
        return messagebox.showinfo("Login", "Incorrect username and/or password.")
        login()

    messagebox.showinfo("Login", "Successful Login. ")
    storage()
    db.close()


def register():
    root.destroy()
    import registerWindow

def login():
    def clear_text():
        entry.delete(0, END)
        entry2.delete(0, END)
    checkframe = ttk.LabelFrame(root, text='Login', width=460, height=300)
    checkframe.place(x=20, y=12)
    emailLogin = ttk.Label(root, text = "Username : ").place(x=120, y=112)
    entry = tk.Entry(root, textvariable=email_var, font=('calibre', 10, 'normal'))
    entry.place(x=190, y=110)
    passwordLogin = ttk.Label(root, text = "Password : ").place(x=125, y=140)
    entry2 = tk.Entry(root, textvariable=pass_var, font=('calibre', 10, 'normal'), show='*')
    entry2.place(x=190, y=140)
    accentbutton = ttk.Button(root, text='Login', style='AccentButton', command=check)
    accentbutton.place(x=210, y=170)
    accentbutton = ttk.Button(root, text='Register', style='AccentButton', command=register)
    accentbutton.place(x=210, y=210)

login()



root.mainloop()