from tkinter import *

def add():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    add = num1 + num2
    value.config(text=add)

win = Tk()
win.geometry('400x500')
win.title("Simple Calculator")

num1_label = Label(win, text="1st num").grid(row=0, column=0)
num1_entry = Entry(win)
num1_entry.grid(row=0, column=1)

num2_label = Label(win, text="num2").grid(row=1, column=0)
num2_entry = Entry(win)
num2_entry.grid(row=1, column=1)

add_btn = Button(win, text="add", command=add).grid(row=2, column=0)
subs_btn = Button(win, text="subs", command=add).grid(row=3, column=0)
multi_btn = Button(win, text="multi", command=add).grid(row=4, column=0)
division_btn = Button(win, text="add", command=add).grid(row=5, column=0)

result_label = Label(win, text="Result: ").grid(row=3, column=1, columnspan=2)
value = Label(win, text="")
value.grid(row=3, column=2, columnspan=2)

win.mainloop()
