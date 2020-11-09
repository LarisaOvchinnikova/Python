from tkinter import *
from tkinter import ttk

def add():
    result.insert(0, int(num1.get()) + int(num2.get()))


root = Tk()
root.title("Sum")
mainframe = ttk.Frame(root, padding="10")
mainframe.grid(column=3, row=3)

# создадим окна для ввода чисел
num1 = Entry(root)
num1.grid(row=0, column=1)

num2 = Entry(root)
num2.grid(row=0, column=2)

ttk.Button(root, text="Sum", command=add).grid(row=2, column=0, columnspan=3)

# создадим окно для вывода результата
result = Entry(root, width=33)
result.grid(row=3, column=0, columnspan=5)

root.mainloop()