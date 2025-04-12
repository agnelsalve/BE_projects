from tkinter import *
from tkinter.ttk import *

from time import strftime

r = Tk()
r.title("Digital Clock")

def time():
    s = strftime('%m/%d/%Y,%H:%M:%S %p')
    label.config(text=s)
    label.after(1000, time)

label = Label(r,font =("ds-digital",100),background="black",foreground="red")
label.pack(anchor='center')
time()
mainloop()
