import time
from tkinter import *

from datetime import datetime

# define some colors
cor1 = "#3d3d3d" #red
cor2 = "#21c25c" #black


root = Tk()
root.title("")
root.geometry("431x180")
root.configure(background=cor1)
root.resizable(width=FALSE, height=FALSE)

def clock():
    time = datetime.now()
    hour = time.strftime("%H:%M:%S")
    weekday = time.strftime("%A")
    day = time.day
    month = time.strftime("%B")
    year = time.strftime("%Y")
    l1.config(text=hour)
    l1.after(200, clock)

    l2.config(text= weekday + "" + str(day) + "/" + str(month) + "/" + (year))



l1 = Label(root, font=('Arial 80'), bg=cor1, fg=cor2)
l1.grid(row=0, column=0, sticky=NW)

l2 = Label(root, font=('Arial 20'), bg=cor1, fg=cor2)
l2.grid(row=1, column=0, sticky=NW)
clock()
root.mainloop()
