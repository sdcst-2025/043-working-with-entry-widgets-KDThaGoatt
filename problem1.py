"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""


import tkinter as tk
from tkinter import *

def toggle1(e):
    text = b1["text"]
    if text == "+":
        b1.config(text="-")
    if text == "-":
        b1.config(text="+")

def toggle2(e):
    text = b2["text"]
    if text == "+":
        b2.config(text="-")
    if text == "-":
        b2.config(text="+")

def factor(e):
    posneg1 = b1["text"]
    posneg2 = b2["text"]
    data1 = e1.get()
    data2 = e2.get()
    
    data1 = int(data1)
    data2 = int(data2)
    
    if posneg1 == "-":
        data1 = -data1
    if posneg2 == "-":
        data2 = -data2

    factors = []
    for i in range(-abs(data2) - 1, abs(data2) + 1):
        if i != 0 and data2 % i == 0:
            n = data2 // i
            if n + i == data1:
                posneg3 = False
                posneg4 = False
                factors.append((i, n))
                if i < 0:
                    posneg3 = True
                if n < 0:
                    posneg4 = True
                if posneg3 == True:
                    posneg3 = "-"
                if posneg3 == False:
                    posneg3 = "+"
                if posneg4 == True:
                    posneg4 = "-"
                if posneg4 == False:
                    posneg4 = "+"
                print(factors)
                answer = (f"x {posneg3} {factors[0][0]}, x {posneg4} {factors[0][1]}")
                print(answer)

win = tk.Tk()
win.geometry("393x100")

l1 = tk.Label(text="Enter the values for b and c from your trinomial into the entry boxes", borderwidth=3, relief="groove")
l2 = tk.Label(width=17, text="x²", borderwidth=2, relief="groove")
e1 = tk.Entry(width=10, borderwidth=2, relief="groove", justify="right")
l3 = tk.Label(width=10, text="x", borderwidth=2, relief="groove", anchor=W)
e2 = tk.Entry(width=20, borderwidth=2, relief="groove", justify="right")
e3 = tk.Entry(width=23, borderwidth=2, relief="groove")
b1 = tk.Button(text="+")
b2 = tk.Button(text="+")
b3 = tk.Button(text="Factor", justify="center", width=19)

l1.grid(row=0,column=0,columnspan=3, sticky=N)
l2.grid(row=1, column=0, sticky=W)
e1.grid(row=1, column=1, sticky=W)
l3.grid(row=1, column=1, sticky=E)
e2.grid(row=1,column=2, sticky=E)
b1.grid(row=1,column=0, sticky=E)
b2.grid(row=1,column=2, sticky=W)
b3.grid(row=2, column=1)
e3.grid(row=3, column=1, columnspan=2, sticky=W)

b1.bind("<Button-1>", toggle1)
b2.bind("<Button-1>", toggle2)
b3.bind("<Button-1>", factor)

win.mainloop()