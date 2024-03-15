import tkinter as tk
from tkinter import ttk
import time

def main():
    #* define screen --------------------------------
    root =  tk.Tk()
    root.configure(padx=32,pady=8)
    
    bottom_frame = ttk.Frame(root, name="time loging").grid(column=0,row=1)
    ttk.Label(bottom_frame, text="hello world").grid(column=1,row=0,padx=10,pady=10)
    root.mainloop()
    
if __name__ == '__main__':
    main()
