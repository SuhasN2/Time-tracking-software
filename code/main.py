import tkinter as tk
from tkinter import ttk
from datetime import datetime
import json 

def main():

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
        global task_start_time, task_end_time
        
        data = tasks
        new_log = {
        "start_time": task_start_time,
        "end_time": task_end_time,
        "commit_comment": commit_common_text.get()
        }
        
        data[Task_selected.get()]["logs"].append(new_log) #* For some reason interpreter is thinking 
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
        except:
            print("Error(virtual cannot be closed)")
        Reset_logs()
        print("log data Finished successfully")


    def start_timer():
        global task_start_time 
        task_start_time = str(datetime.today())
        print(task_start_time)
        ttk.Button(bottom_frame, text="end", command=end_timer ).grid(column=2,row=0)

    def end_timer():
        global task_end_time, commit_common
        task_end_time = str(datetime.today())
        popup_window = tk.Toplevel()
        ttk.Label(popup_window, text="brief Description of Completed task").grid(columnspan=2,row=0,column=0)
        commit_common = ttk.Entry(popup_window)
        commit_common.grid(column=0,row=1)

        ttk.Button(popup_window, text="enter",command=lambda:log_data(TASKS,commit_common,popup_window)).grid(column=1,row=1)
        
    # define screen --------------------------------
    root =  tk.Tk()
    Task_selected = tk.StringVar()
    root.configure(padx=32,pady=8)
    task_start_time = ""
    task_end_time = ""

    # define frame --------------------------------
    bottom_frame = ttk.Frame(root, name="time loging").grid(column=0,row=0)
    ttk.OptionMenu(bottom_frame,Task_selected,*list(TASKS.keys())).grid(bottom_frame,column=1,row=0,padx=10,pady=10)
    ttk.Button(bottom_frame, text="Start", command=start_timer ).grid(column=2,row=0)

    root.mainloop()
    #todo Break down larger functions into smaller,
    #* Close window automatically when clicked enter
if __name__ == '__main__':
    main()
