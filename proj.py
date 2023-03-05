import time
from plyer import notification

def noti():
    notification.notify(
    title = txt_in1.get(),
    message = txt_in2.get('1.0',END),
    app_icon = "D:\Python_Programs\projectDesktopNotifier\iconfinder-bellnotificationsnoticenotifyalert-3993856_112639.ico",
    timeout = 30
    )

from datetime import datetime
def timer():
    while (True):
        now = datetime.now()
        current_time = now.strftime("%H:%M")

        now_hour = current_time[:2]
        now_minute = current_time[3:]

        req_hour = hour.get()
        req_minute = minute.get()
        
        #diff_hour = req_hour - now_hour
        #diff_minute = req_minute - now_minute

        if (req_hour == now_hour and req_minute == now_minute):
            noti()
            break



from tkinter import *

"""both these statements give title to the window created by Tk() object
#root = Tk(className="Notifier")     this always makes the 1st letter small
#root.title("Notifier")"""


root = Tk()
root.title("Notifier")
root.config(bg="#cce1ec")
root.geometry("700x400")
root.resizable(False,False)


top = Label(root,text="Desktop Notifier",font=("times new roman",25,"bold"),bg="#cce1ec",fg="black").place(x=200,y=0)


lb1 = Label(root,text="Reminder Title",font=("times new roman",10))
lb1.place(x=10,y=100)
txt_in1 = Entry(root,font=("times new roman",10))
txt_in1.place(x=250,y=100)

lb2 = Label(root,text="Reminder Message",font=("times new roman",10)).place(x=10,y=150)
txt_in2 = Text(root,font=("times new roman",10))
txt_in2.place(x=250,y=150,width=200,height=100)

lb3 = Label(root,text="Select Time(in 24 hour format hh:mm)",font=("times new roman",10)).place(x=10,y=270)
hour = Spinbox(root, from_ =0, to = 23)
hour.place(x=250,y=270)
minute = Spinbox(root, from_ =0, to = 59)
minute.place(x=400,y=270)

btn1 = Button(root,text="SAVE",bg="white",fg="black",font=("times new roman",15,"bold"),activebackground="gray",command=timer).place(x=300,y=350,width=80,height=40)

root.mainloop()


