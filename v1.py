try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

from functools import partial
from tkinter import *
import tkinter

tk = tkinter.Tk()
tk.title("Ocscreen keyboard")

tk['bg'] = 'purple'
# tk.resizable(0,0)


def select(value):
    if value == "Space":
        entry.insert(tkinter.END, '  ')
    else:
        entry.insert(tkinter.END, value)


label = Label(tk, text="Onscreen keyboard", font=('arial', 20, 'bold'),
              bg='purple', fg="#000000").grid(row=0, columnspan=40)
entry = Entry(tk, width=138, font=('arial', 10, 'bold'))
entry.grid(row=1, columnspan=40)

buttons = [
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
    'z', 'x', 'c', 'v', 'b', 'n', 'm', '_',
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
    'Space']

r = 2
c = 2


for b in buttons:
    command = lambda x=b: select(x)
    if b != "Space":
        tkinter.Button(tk, text=b, width=5,
                       command=command).grid(row=r, column=c)

    if b == "Space":
        tkinter.Button(tk, text=b, width=115, padx=3, pady=3,
                       bd=12, command=command).grid(row=7, column=c)

    c += 1

    if c > 10 and r == 2:
        c = 2
        r += 1
    if c > 10 and r == 3:
        c = 2
        r += 1
    if c > 10 and r == 4:
        c = 2
        r += 1
    # if c > 5 and r == 5:
    #     c = 0
    #     r += 1


tk.mainloop()
