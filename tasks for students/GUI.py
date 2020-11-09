from tkinter import *
from tkinter import ttk

def add():
    pass


root = Tk()
root.title("Sum")
mainframe = ttk.Frame(root, padding="10")
mainframe.grid(column=3, row=3)

# создадим окно для ввода
num1 = Entry(root, width=33)
num1.grid(row=0, column=2, columnspan=2)

ttk.Button(root, text="Sum", command=add).grid(row=1, column=1)

root.mainloop()