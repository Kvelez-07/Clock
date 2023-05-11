from tkinter import *
from time import *

def update():

    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)
    #Clock updates
    time_label.after(1000, update)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

window = Tk()

time_label = Label(window, font=("Arial", 50), fg="blue", bg="white")
time_label.pack()

day_label = Label(window, font=("Ink Free", 15), fg="blue", bg="white")
day_label.pack()

date_label = Label(window, font=("Ink Free", 20), fg="blue", bg="white")
date_label.pack()

update()
window.mainloop()