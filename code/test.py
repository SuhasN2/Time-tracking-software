from tkinter import *
from tkinter import ttk

root = Tk()

# Correct usage of StringVar
my_string_var = StringVar()
my_string_var.set("Hello, world!")

print(type(my_string_var.get()))
# Example widget using StringVar
my_label = ttk.Label(root, textvariable=my_string_var)
my_label.grid(row=0, column=0)

root.mainloop()
