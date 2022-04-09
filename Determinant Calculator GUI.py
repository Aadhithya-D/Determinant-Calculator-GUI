from tkinter import *
import numpy as np
import math
from tkinter import messagebox

win = Tk()
win.title("DETERMINANT CALCULATOR")
win_width = win.winfo_reqwidth()
win_height = win.winfo_reqheight()
pos_right = int(win.winfo_screenwidth() / 2 - win_width / 2)
pos_down = int(win.winfo_screenheight() / 2 - win_height / 2)
win.geometry("+{}+{}".format(pos_right, pos_down))


def determinant():
    try:
        e = element_entry.get()
        e1 = str(e).split()
        c = []
        n = len(e1)
        m = math.sqrt(n)
        if e == "":
            messagebox.showerror("Enmpty matrix", "Please enter a matrix", parent=win)
        elif m.is_integer():
            global win2
            win2 = Tk()
            win2.title("Answer!!")
            for row in e1:
                b = int(row)
                c.append(b)

            def divide_chunks(l, n):
                for i in range(0, len(l), n):
                    yield l[i:i + n]

            matrix = list(divide_chunks(c, int(m)))
            output_label = Label(win2, text="The determinant of the entered matrix " + str(matrix) + " is " + str(np.linalg.det(matrix)), font=("calibre", 15))
            output_label.pack(pady=10, padx=10)
        else:
            messagebox.showerror("Not square matrix", "The matrix entered is not a square matrix", parent=win)
    except:
        messagebox.showerror("Not square matrix", "The matrix entered is not a square matrix", parent=win)


def clear():
    try:
        element_entry.delete(0, END)
        win2.destroy()
    except:
        element_entry.delete(0, END)


def how():
    win1 = Tk()
    win1.title("How to use?")
    warning_label = Label(win1, text="*Only square matrix should be entered*", font=("calibre", 15))
    warning_label1 = Label(win1, text="*After each element leave a space*", font=("calibre", 15))
    warning_label2 = Label(win1, text="*Click \"Clear\" before entering the next matrix*", font=("calibre", 15))
    warning_label.pack(padx=10, pady=(20, 10))
    warning_label1.pack(padx=10, pady=(10, 20))
    warning_label2.pack(padx=10, pady=(10, 20))


matrix_label = Label(win, text="Enter the matrix:", font=("calibre", 15))
element_entry = Entry(win, width=50)
how_button = Button(win, text="How to use?", font=("calibre", 10), command=how)
element_button = Button(win, text="Enter", font=("calibre", 15), command=determinant)
clear_button = Button(win, text="Clear", font=("calibre", 15), command=clear)
how_button.grid(row=0, column=0, columnspan=2, pady=10)
matrix_label.grid(row=1, column=0, padx=10, pady=10)
element_entry.grid(row=1, column=1, padx=10, pady=10)
element_button.grid(row=2, column=1, padx=10, pady=10)
clear_button.grid(row=2, column=0, padx=10, pady=10)
win.mainloop()
