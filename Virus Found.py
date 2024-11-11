from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("200x200")

def msg():
    messagebox.showwarning("alert", "Virus Found")
button = Button(window, text ="Scan", command = msg)
button.pack()

window.mainloop()