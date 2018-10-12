from tkinter import *
from tkinter import ttk

master = Tk()
Label(master, text="First Name").grid(row=5, column= 10)
Label(master, text="Daft.ie Bot").grid(row=3,column=10)

e1=Entry(master)

e1.grid(row=5, column=11)

mainloop()
