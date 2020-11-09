# 1)импортируем нужную библиотеку
# 2)создаем окно
# 3)создаем кнопки
# 4)создаем калькулятор:
# а)исключаем возможность введения букв
# б)добавляем влзможность счета 9основная часть программы)
# в)добавляем кнопку очистить
#from terminal run:  python -m tkinter


# 1)импортируем нужную библиотеку
from tkinter import *
from tkinter import messagebox
from tkinter import ttk            # (для кнопок)

# 2)создаем окно
root = Tk()
root.title("Calculator")
# root.mainloop()  # запускаем, проверяем, появилось ли окно
# 4) создаем логику калькулятора
# переменные создаваемые внутри функции - имеют локальную область видимости
# чтобы иметь возможность изменять глобальные пременные внутри функции
# эти переменные следует определить в теле функции с помощью инструкции global

def calc(key):
    global memory
    if key == "=":
# исключаем написание букв
        strl = "0123456789.+-*/"  # возможные символы
        if calc_entry.get()[0] not in strl:
            calc_entry.insert(END, "The symbol is not allowed!")
            messagebox.showerror("Error!", "You entered wrong symbol.")
# eval выполняет выражение записанное в строке
# счет
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "ERROR!")
            messagebox.showerror("Error!", "Check your input data")
# очистить поле
    elif key == "C":
        calc_entry.delete(0, END)
# смена +/-
    elif key == "-/+":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
# кнопка стирания последнего символа (моя)
    elif key == "Backspace":
        calc_entry.delete(len(calc_entry.get())-1)
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)

# 3)создаем кнопки
# Создаем список кнопок
bttn_list = [
    "7", "8", "9", "+", "-",
    "4", "5", "6", "*", "/",
    "1", "2", "3", "-/+", "=",
    "0", ".", "C", "**", "Backspace"
]
r = 1
c = 0

for i in bttn_list:
    # rel = ""
    cmd = lambda x=i: calc(x)
    ttk.Button(root, text=i, command=cmd).grid(row=r, column=c)
    c += 1
    if c > 4:
        c = 0
        r += 1

# создадим окно для ввода
calc_entry = Entry(root, width=33)
calc_entry.grid(row=0, column=0, columnspan=5)


root.mainloop()
