from tkinter import *

"""both these statements give title to the window created by Tk() object
#root = Tk(className="Notifier")     this always makes the 1st letter small
#root.title("Notifier")"""


root = Tk()
root.title("Notifier")
root.config(bg="black")
root.geometry("800x500")
root.resizable(False,False)


top = Label(root,text="Desktop Notifier",font=("times new roman",25,"bold"),bg="black",fg="white").place(x=200,y=0)


lb1 = Label(root,text="Reminder Title",font=("times new roman",10)).place(x=0,y=100)
txt_in1 = Entry(root,font=("times new roman",10))
txt_in1.place(x=250,y=100)

lb2 = Label(root,text="Reminder Message",font=("times new roman",10)).place(x=0,y=150)
txt_in1 = Text(root,font=("times new roman",10))
txt_in1.place(x=250,y=150,width=200,height=100)

lb3 = Label(root,text="Select Time(in 24 hour format hh:mm)",font=("times new roman",10)).place(x=0,y=270)
hour = Spinbox(root, from_ =0, to = 23)
hour.place(x=250,y=270)
minute = Spinbox(root, from_ =0, to = 59)
minute.place(x=400,y=270)

btn1 = Button(root,text="SAVE",bg="gray",fg="pink",font=("times new roman",20,"bold"),activebackground="light blue").place(x=100,y=420,width=100,height=50)

root.mainloop()