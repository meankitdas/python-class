from tkinter import *
from tkinter import messagebox
import numpy as np

#create the main window
win=Tk()
win.geometry("400x250")
win.title("simple calculator")
def add():
    num1=float(num1_entry.get())
    num2=float(num2_entry.get())
    result=num1+num2
    result_value.config(text=result)
    
def subs():
    num1= float(num1_entry.get())
    num2=float(num2_entry.get())
    result=num1-num2
    result_value.config(text=result)
    
def mul():
    num1= float(num1_entry.get())
    num2=float(num2_entry.get())
    result=num1*num2
    result_value.config(text=result)
    
def div():
    num1= float(num1_entry.get())
    num2=float(num2_entry.get())
    if num2==0:
        messagebox.showerror("Error","Divide by 0 is not possible")
    else:
        result=num1/num2
        result_value.config(text=result)
        
def log():
    num1= num1_entry.get()
    num2= num2_entry.get()
    if num1:
        num1 = float(num1)
        result = np.log([num1])
        result_value.config(text=result)
    else:
        num2 = float(num2)
        result = np.log([num2])
        result_value.config(text=result)
        

    
num1_label=Label(win,text="Number 1").grid(row=0,column=0)
num1_entry=Entry(win)
num1_entry.grid(row=0,column=1)

num2_label=Label(win,text="Number 2").grid(row=1,column=0)
num2_entry=Entry(win)
num2_entry.grid(row=1,column=1)

add_button=Button(win,text="Add",command=add).grid(row=2,column=0)
subs_button=Button(win,text="Subs",command=subs).grid(row=2,column=1)
mul_button=Button(win,text="Mul",command=mul).grid(row=2,column=2)
div_button=Button(win,text="Div",command=div).grid(row=2,column=3)
log_button=Button(win,text="Log",command=log).grid(row=2,column=4)

result_label=Label(win,text="Result:")
result_label.grid(row=3,column=0,columnspan=2)
result_value = Label(win,text="")
result_value.grid(row=3,column=1,columnspan=2)
win.mainloop()