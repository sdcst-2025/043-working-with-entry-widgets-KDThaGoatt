#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""

import tkinter as tk
from tkinter import *
import math

def run(e):
    data1 = e1.get()
    data2 = e1.get()
    data1 = int(data1)
    data2 = int(data2)
    hyp = math.sqrt(data1**2 + data2**2)
    hyp = round(hyp, 6)
    e3.delete(0,tk.END)
    e3.insert(0,hyp)

win = tk.Tk()
win.geometry("600x500")

triangle = PhotoImage(file="triangle.png")

l1 = tk.Label(text="Enter short sides of triangle to get hypotenuse")
l2 = tk.Label(win, image=triangle)
e1 = tk.Entry(win, width=15, borderwidth=5, relief="raised", justify="center")
e2 = tk.Entry(win, width=15, borderwidth=5, relief="raised", justify="center")
e3 = tk.Entry(win, width=15, borderwidth=5, relief="sunken", justify="center")
b1 = tk.Button(win, width=10, text="Calculate")

b1.bind("<Button-1>", run)

l1.pack()
l2.pack()
e1.place(x=45, y=240)
e2.place(x=235, y=385)
e3.place(x=283, y=240)
b1.place(x=178, y=240)

win.mainloop()