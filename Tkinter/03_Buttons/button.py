from tkinter import *

root = Tk()

def on_custom_height_width_button_click():
    label = Label(root, text="You have clicked on custom height & width button!")
    label.pack()

disabled_button = Button(root, text="Click Me!", state=DISABLED)
disabled_button.pack()

custom_height_width_button = Button(
    root, text="Custom Button", 
    padx=20, 
    pady=10, 
    borderwidth=2,
    bg="red",
    fg="#000000",
    command=on_custom_height_width_button_click,
)
custom_height_width_button.pack()

root.mainloop()