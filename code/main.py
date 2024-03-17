import tkinter as tk
from tkinter import ttk
from datetime import datetime
import json 

def main():

    CURRENT_TASK = 0
    Temporary_start_time = ""
    Temporary_end_time = ""
    commit_common = ""

    #* open tasks.json --------------------------------
    try:
        with open(r"code\tasks.json", "r") as file:
            TASKS = json.load(file)
            print (TASKS)
    except FileNotFoundError:
        print (f"tasks.json not found\n {FileNotFoundError}")

    def log_data(context):
        global Temporary_start_time, Temporary_end_time, commit_common

        # Make a copy of the current task data
        current_task_data = context[(list(context.keys())[CURRENT_TASK])]
        current_task_data["logs"].append({
            "start time": Temporary_start_time,
            "end time": Temporary_end_time,
            "commit common": commit_common.get()
        })

        # Update the TASKS dictionary with the modified task data
        TASKS[(list(TASKS.keys())[CURRENT_TASK])] = current_task_data

        # Save the updated TASKS dictionary to the file
        with open(r"code\tasks.json", "w") as file:
            json.dump(TASKS, file)

    def start_timer():
        global Temporary_start_time 
        Temporary_start_time = datetime.today()
        print(Temporary_start_time)
        ttk.Button(bottom_frame, text="end", command=end_timer ).grid(column=2,row=0)

    def end_timer():
        global Temporary_end_time, commit_common
        Temporary_end_time = datetime.today()
        print(Temporary_end_time)
        popup_window = tk.Toplevel()
        ttk.Label(popup_window, text="brief Description of Completed task").grid(columnspan=2,row=0,column=0)
        commit_common = ttk.Entry(popup_window,)
        commit_common.grid(column=0,row=1) 
        print(commit_common)
        ttk.Button(popup_window, text="enter",command=lambda:log_data(TASKS)).grid(column=1,row=1)  
        
    #* define screen --------------------------------
    root =  tk.Tk()
    root.configure(padx=32,pady=8)
    
    #* define frame --------------------------------
    bottom_frame = ttk.Frame(root, name="time loging").grid(column=0,row=0)
    ttk.Label(bottom_frame, text=(list(TASKS.keys())[CURRENT_TASK])).grid(column=1,row=0,padx=10,pady=10)
    ttk.Button(bottom_frame, text="Start", command=start_timer ).grid(column=2,row=0)

    root.mainloop()
    
    #todo: Ability to Create a new task new entry window
    #todo: Ability to Log time

if __name__ == '__main__':
    main()
