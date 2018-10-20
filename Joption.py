from tkinter import *
from tkinter import ttk

master = Tk()
master.title("Daft.ie Bot")
master.configure(background='#6ffc6e')
master.geometry("1000x1000")

Label(master, background="#6ffc6e", font = "Verdana 30 bold", text="Daft.ie Bot" ).place(x=520, y=20, anchor="center")
Label(master, background="#6ffc6e", font ="Verdana 10 bold", text="URL").place(x=510, y=50)
Label(master, background="#6ffc6e", font ="Verdana 10 bold", text="Name").place(x=500, y= 100)
Label(master, background="#6ffc6e", font ="Verdana 10 bold", text="Email Address").place(x=475, y=150)
Label(master, background="#6ffc6e", font ="Verdana 10 bold", text="Phone Number").place(x=475, y=200)
Label(master, background="#6ffc6e", font ="Verdana 10 bold", text="Your Message").place(x=475, y=250)
Label(master, background="#6ffc6e", font ="Verdana 10 bold", text="URL").place(x=500, y=375)

e1=Entry(master, background='#ffffff')
e2=Entry(master, background="#ffffff")
e3=Entry(master, background="#ffffff")
e4=Text(master, background="#ffffff")
e5=Entry(master,background="#ffffff")

e1.place(x=450, y=75, width=150)
e2.place(x=450, y=125, width=150)
e3.place(x=450, y=175, width=150)
e4.place(x=375, y=275, width=300, height=150)
e5.place(x=450, y=225, width=150)

button=Button(master, text="Start Bot")
button.place(x=500, y=450)

mainloop()
