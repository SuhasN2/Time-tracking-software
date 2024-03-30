import tkinter as tk
from tkinter import ttk
from datetime import datetime
import json 

def main():

    CURRENT_TASK = 0
    Temporary_start_time = ""
    Temporary_end_time = ""

    #* open tasks.json --------------------------------
    try:
        with open(r"code\tasks.json", "r") as file:
            TASKS = json.load(file)
            print (TASKS)
    except FileNotFoundError:
        print (f"tasks.json not found\n {FileNotFoundError}")    

    def Reset_logs():
        ttk.Button(bottom_frame, text="Start", command=start_timer ).grid(column=2,row=0)

    def log_data(tasks,commit_common_text,popup_window): #* The error "NameError: name 'TASKS' is not defined"
        #? indicates the log_data function can't find the variable tasks
        global Temporary_start_time, Temporary_end_time
        
        data = tasks
        current_task_data = (list(data.keys())[CURRENT_TASK]) # Find the Current task
        

        print (":-",current_task_data,commit_common_text)

        new_log = {
        "start_time": Temporary_start_time,
        "end_time": Temporary_end_time,
        "commit_comment": commit_common_text.get()
        }
        
        data[current_task_data]["logs"].append(new_log) #* For some reason interpreter is thinking 
        print (data)
        #* it's a dictionary

        # Save the updated tasks dictionary to the file
        print("looding",end="\r")
        try:
            with open(r"code\tasks.json", "w") as file:
                json.dump(data, file, indent=4)
            print("Data saved successfully to task.json")
        except Exception as e:
            print("Error saving data:", e)
        try:
            popup_window.destroy()
        except NameError:
            print("Error(virtual cannot be closed)")
        Reset_logs()
        print("log data Finished successfully")


    def start_timer():
        global Temporary_start_time 
        Temporary_start_time = str(datetime.today())
        print(Temporary_start_time)
        ttk.Button(bottom_frame, text="end", command=end_timer ).grid(column=2,row=0)

    def end_timer():
        global Temporary_end_time, commit_common
        Temporary_end_time = str(datetime.today())
        popup_window = tk.Toplevel()
        ttk.Label(popup_window, text="brief Description of Completed task").grid(columnspan=2,row=0,column=0)
        commit_common = ttk.Entry(popup_window)
        commit_common.grid(column=0,row=1)

        ttk.Button(popup_window, text="enter",command=lambda:log_data(TASKS,commit_common,popup_window)).grid(column=1,row=1)
        
    # define screen --------------------------------
    root =  tk.Tk()
    root.configure(padx=32,pady=8)
    
    # define frame --------------------------------
    bottom_frame = ttk.Frame(root, name="time loging").grid(column=0,row=0)
    ttk.Label(bottom_frame, text=(list(TASKS.keys())[CURRENT_TASK])).grid(column=1,row=0,padx=10,pady=10)
    ttk.Button(bottom_frame, text="Start", command=start_timer ).grid(column=2,row=0)

    root.mainloop()
    
    #todo: Close window automatically when clicked enter

if __name__ == '__main__':
    main()
