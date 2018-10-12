from tkinter import *
from tkinter import ttk

master = Tk()
master.title("Daft.ie Bot")
master.configure(background='#9cd2bc')
master.geometry("1000x1000")

Label(master, background="#9cd2bc", font = "Verdana 30 bold", text="Daft.ie Bot" ).place(x=520, y=20, anchor="center")
Label(master, background="#9cd2bc", text="Name").place(x=500, y=50)
Label(master, background="#9cd2bc", text="Email Address").place(x=487, y= 100)
Label(master, background="#9cd2bc", text="Phone Number").place(x=487, y=150)
Label(master, background="#9cd2bc", text="Your Message").place(x=490, y=200)

e1=Entry(master, background='#ffdb6f')
e2=Entry(master, background="#ffdb6f")
e3=Entry(master, background="#ffdb6f")
e4=Entry(master, background="#ffdb6f")

e1.place(x=465, y=75)
e2.place(x=465, y=125)
e3.place(x=465, y=175)
e4.place(x=465, y=225)

mainloop()
