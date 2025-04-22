"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""

import tkinter as tk

def run(e):
    data1 = e1.get()
    data2 = e2.get()
    data3 = e3.get()
    combine = (f"{data1}, {data2}, Grade {data3}")
    e4.delete(0,tk.END)
    e4.insert(0,combine)    

win = tk.Tk()
win.geometry("283x150")

l1 = tk.Label(win, text="Name")
e1 = tk.Entry(win, width=15)
l2 = tk.Label(win, text="Student Number")
e2 = tk.Entry(win, width=15)
l3 = tk.Label(win, text="Grade")
e3 = tk.Entry(win, width=15)
b1 = tk.Button(win, width=10, text="Enter")
e4 = tk.Entry(win, width=47, justify="center")

b1.bind("<Button-1>",run)

l1.grid(row=0, column=0)
e1.grid(row=1, column=0)
l2.grid(row=0, column=1)
e2.grid(row=1, column=1)
l3.grid(row=0, column=2)
e3.grid(row=1, column=2)
b1.place(x=100, y=60)
e4.place(x=0, y=100)

win.mainloop()