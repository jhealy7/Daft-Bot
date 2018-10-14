from tkinter import *
from tkinter import ttk

master = Tk()
master.title("Daft.ie Bot")
master.configure(background='#6ffc6e')
master.geometry("1000x1000")

Label(master, background="#6ffc6e", font = "Verdana 30 bold", text="Daft.ie Bot" ).place(x=520, y=20, anchor="center")
Label(master, background="#6ffc6e", text="Name").place(x=500, y=50)
Label(master, background="#6ffc6e", text="Email Address").place(x=487, y= 100)
Label(master, background="#6ffc6e", text="Phone Number").place(x=487, y=150)
Label(master, background="#6ffc6e", text="Your Message").place(x=490, y=200)

e1=Entry(master, background='#ffffff')
e2=Entry(master, background="#ffffff")
e3=Entry(master, background="#ffffff")
e4=Text(master, background="#ffffff")

e1.place(x=450, y=75, width=150)
e2.place(x=450, y=125, width=150)
e3.place(x=450, y=175, width=150)
e4.place(x=375, y=225, width=300, height=150)

button=Button(master, text="Start Bot")
button.place(x=500, y=400)

mainloop()
