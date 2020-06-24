import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("SREC security sys")
l1 = Label(window, text="CRIMINAL IDENTIFIED", font=('ArialBold', 10), fg="blue")
window.geometry('500x100')
l1.grid(column=0, row=0)
l2= Label(window, text="""*ALERT*""",font=('ArialBold',50),fg="red")
l2.grid(column=20, row=80)


window.mainloop()
