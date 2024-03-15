import tkinter as tk
from tkinter import ttk
from datetime import datetime
from json import load

def main():

    Current_task = 0

    #* open tasks.json --------------------------------
    with open(r"tasks.json", "r") as file:
        tasks = load(file)
        print(tasks)

    #* define screen --------------------------------
    root =  tk.Tk()
    root.configure(padx=32,pady=8)
    
    #* define frame --------------------------------
    bottom_frame = ttk.Frame(root, name="time loging").grid(column=0,row=1)
    ttk.Label(bottom_frame, text=(list(tasks.keys())[0])).grid(column=1,row=0,padx=10,pady=10)

    root.mainloop()
    
    #todo: Ability to Create a new task 
    #todo: Ability to Log time

if __name__ == '__main__':
    main()
