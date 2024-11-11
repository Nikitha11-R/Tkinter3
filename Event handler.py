from tkinter import *

window = Tk()
window.geometry("200x200")

def handle_keypress(event):
    print(event.char)

window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("Button has been clicked.")

button = Button(text="click Here")
button.pack()

button.bind("<Button-1>", handle_click)

window.mainloop()