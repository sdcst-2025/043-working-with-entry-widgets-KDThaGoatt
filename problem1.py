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

win = tk.Tk()
win.geometry("364x300")

var1 = tk.StringVar(value="x²")
var2 = tk.StringVar(value="x")

l1 = tk.Label(text="Enter the values for b and c from your trinomial into the entry boxes", borderwidth=3, relief="groove")
e1 = tk.Entry(width=20, textvariable=var1, borderwidth=2, relief="groove")
e2 = tk.Entry(width=20, textvariable=var2, borderwidth=2, relief="groove")
e3 = tk.Entry(width=20, borderwidth=2, relief="groove")
e4 = tk.Entry(width=20, borderwidth=2, relief="groove")
b1 = tk.Button(text="+")
b2 = tk.Button(text="+")
b3 = tk.Button(text="Factor", justify="center", width=10)

l1.grid(row=0,column=0,columnspan=3, sticky=W)
e1.grid(row=1, column=0, sticky=W)
e2.grid(row=1, column=1,sticky=W)
e3.grid(row=1,column=2,sticky=W)
b1.grid(row=1,column=0, sticky=E)
b2.grid(row=1,column=1,sticky=E)
b3.grid(row=2, column=1)
e4.grid(row=3, column=1, columnspan=2,sticky=W)

b1.bind("<Button-1>", toggle1)
b2.bind("<Button-1>", toggle2)

win.mainloop()
