from tkinter import *

root = Tk()

def on_button_click():
    label = Label(root, text="Hello " + input_field.get())
    label.pack()

input_field = Entry(root, width=50, bg="grey", borderwidth=2)
input_field.insert(0, "Enter your name")
input_field.pack()

button = Button(root, text="click me!", padx=20, pady=10, borderwidth=2, command=on_button_click)
button.pack()

root.mainloop()