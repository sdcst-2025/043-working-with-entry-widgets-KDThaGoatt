#!python3

"""
Create the interface shown.  The program should be able to perform the math operation specified
by the buttons and display the entry in the 3rd entry widget;
"""

import tkinter as tk

def mult(e):
    data1 = e1.get()
    data2 = e2.get()
    data1 = int(data1)
    data2 = int(data2)
    ans = data1 * data2
    e3.delete(0,tk.END)
    e3.insert(0,ans)

def add(e):
    data1 = e1.get()
    data2 = e2.get()
    data1 = int(data1)
    data2 = int(data2)
    ans = data1 + data2
    e3.delete(0,tk.END)
    e3.insert(0,ans)

def minus(e):
    data1 = e1.get()
    data2 = e2.get()
    data1 = int(data1)
    data2 = int(data2)
    ans = data1 - data2
    e3.delete(0,tk.END)
    e3.insert(0,ans)

def div(e):
    data1 = e1.get()
    data2 = e2.get()
    data1 = int(data1)
    data2 = int(data2)
    ans = data1 / data2
    e3.delete(0,tk.END)
    e3.insert(0,ans)


w = tk.Tk()
w.attributes("-topmost",True)

l1 = ( tk.Label(w,text="Number 1"))
l2 = ( tk.Label(w,text="Number 2"))
l3 = ( tk.Label(w,text="Number Calculator"))
e1 = ( tk.Entry(w,text=""))
e2 = ( tk.Entry(w,text=""))
e3 = ( tk.Entry(w,text="answer",state='disabled'))
b1 = (tk.Button(w,text="x"))
b2 = (tk.Button(w,text="+"))
b3 = (tk.Button(w,text="-"))
b4 = (tk.Button(w,text="÷"))

b1.bind("<Button-1>", mult)
b2.bind("<Button-1>", add)
b3.bind("<Button-1>", minus)
b4.bind("<Button-1>", div)

l3.grid(row=1,column=1,columnspan=4)
l1.grid(row=2,column=1,columnspan=2)
l2.grid(row=2,column=3,columnspan=2)
e1.grid(row=3,column=1, columnspan=2)
e2.grid(row=3,column=3, columnspan=2)
b1.grid(row=4,column=1)
b2.grid(row=4,column=2)
b3.grid(row=4,column=3)
b4.grid(row=4,column=4)
e3.grid(row=5,column=1,columnspan=4)

w.mainloop()
