from tkinter import *

root = Tk()

my_label_1 = Label(root, text="Hello world!")
my_label_2 = Label(root, text="My name is Zahid Hasan.")

my_label_1.grid(row=0, column=0)
my_label_2.grid(row=1, column=1)

root.mainloop()