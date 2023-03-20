from tkinter import *

root = Tk()
var = StringVar()
var.set("1")

def selection():
    label.config(text="You selected " + var.get())

R1 = Radiobutton(root, text="Option 1", ,variable=var value="1", command=selection)
R1.pack()

R2 = Radiobutton(root, text="Option 2", variable=var, value="2", command=selection)
R2.pack()

label = Label(root)
label.pack()

root.mainloop()