from tkinter import *
from PIL import Image,ImageTk
from tkinter import Scale
import tkinter.messagebox as mi
import datetime
from datetime import date


def days_remain():
    cur = datetime.date.today()
    end = date.fromisoformat("2021-07-31")
    remaindays = end - cur
    Label(root,text="SALARYDAY").grid(row=3,column=2)
    myentry3 = Label(root, text=remaindays)
    myentry3.grid(row=3,column=3)
def days_remain2():
    cur = datetime.date.today()
    end=date.fromisoformat("2021-07-31")
    remaindays=end-cur
    Label(root, text="DSALGO").grid(row=4, column=2)
    myentry3 = Label(root, text=remaindays)
    myentry3.grid(row=4, column=3)

def getval():
    # print("its running")

    # Label(root,text=goalname.get()).grid(row=1, column=0)

    days_remain()
    days_remain2()



root=Tk()
root.title("Goals Measure")
root.geometry("300x300")
# root.wm_iconbitmap("44.ico")
# root.configure(bg="lightblue")
# text=Text(root,bg="white")
# text.pack()
Label(root,text="Goals").grid(row=2,column=2)
Label(root,text="Days remaining").grid(row=2,column=3)
# goalname=StringVar()
# daysremaining=StringVar()
# myentry=Entry(root,textvariable=goalname)
# myentry.grid(row=1,column=0)
# myentry2=Entry(root,textvariable=daysremaining)
# myentry2.grid(row=1,column=2)
getval()
# Label(text=goalname.get()).grid(row=1,column=3)
# Button(root,text="submit",command=getval).grid(row=7,column=3)
root.mainloop()