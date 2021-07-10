from tkinter import *
import datetime
from datetime import date


def days_remain():
    cur = datetime.date.today()
    lines = len(open("goals.txt", "r").readlines())
    # print(lines)
    if lines > 0:
        goals = []
        dates = []
        goals_list = []
        days_list = []
        with open("dates.txt", "r") as f:
            for line in f:
                if line != "":
                    dates.append(line.strip())
        with open("goals.txt", "r") as f:
            for line in f:
                if line != "":
                    goals.append(line.strip())
        for i in range(lines):
            end = date.fromisoformat(dates[i])
            remaindays = end - cur
            myentry = Label(root, text=goals[i])
            myentry.grid(row=i + 3, column=2)
            goals_list.append(myentry)
            mentry = Label(root, text=remaindays)
            mentry.grid(row=i + 3, column=3)
            days_list.append(mentry)


def reset():
    f = open("goals.txt", "r+")

    # absolute file positioning
    f.seek(0)

    # to erase all data
    f.truncate()
    f = open("dates.txt", "r+")

    # absolute file positioning
    f.seek(0)

    # to erase all data
    f.truncate()
    root.destroy()


root = Tk()
root.title("Goals Measure")
root.geometry("350x350")
# root.wm_iconbitmap("44.ico")
Label(root, text="Goals").grid(row=1, column=2)
Label(root, text="Days remaining").grid(row=1, column=3)
goalname = StringVar()
goaldate = StringVar()
entry = Entry(root, textvariable=goalname)
entry.grid(row=2, column=2)
entry2 = Entry(root, textvariable=goaldate)
entry2.grid(row=2, column=3)

# goals = []
# dates = []


def additem():
    # print("its running")

    # Label(root,text=goalname.get()).grid(row=1, column=0)
    with open("goals.txt", "a") as f:
        f.write(f"{goalname.get()}\n")
    with open("dates.txt", "a") as fd:
        fd.write(f"{goaldate.get()}\n")
    days_remain()


days_remain()
Button(root, text="add new", command=additem).grid(row=2, column=4)
Button(root, text="reset", command=reset).grid(row=1, column=4)
root.mainloop()
