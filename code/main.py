import tkinter as tk
from tkinter import ttk
from datetime import datetime
from json import load,dump
import pygame


def main():
    pygame.mixer.init()
    #* open tasks.json --------------------------------
    try:
        with open(r"code\tasks.json", "r") as file:
            TASKS = load(file)
            print (TASKS)
    except FileNotFoundError:
        print (f"tasks.json not found\n {FileNotFoundError}")    

    def Reset_logs():
        ttk.Button(bottom_frame, text="Start", command=start_timer ).grid(column=2,row=0)

    def get_time_difference(start_time, end_time):
        # Convert timestamps to datetime objects
        start_datetime = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S.%f")
        end_datetime = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S.%f")
        # Calculate the difference as a timedelta object
        time_delta = end_datetime - start_datetime
        # Return the difference in seconds
        return time_delta.total_seconds()

    def log_data(tasks,commit_common_text,popup_window): #* The error "NameError: name 'TASKS' is not defined"
        #? indicates the log_data function can't find the variable tasks
        global task_start_time, task_end_time
        
        # todo: Add the ability to create Tasks

        data = tasks
        new_log = {
        "start_time": task_start_time,
        "end_time": task_end_time,
        "commit_comment": commit_common_text.get()
        }
        
        x = Task_selected.get()
        data[Task_selected.get()]["logs"].append(new_log)
        data[x]["Time spent on "] = data[x]["Time spent on "] + get_time_difference(task_start_time, task_end_time)
        print (data)# TODO: How much did I work in a day
        # TODO: The box view or the DAY calendar view

        # Save the updated tasks dictionary to the file
        print("looding")
        try:
            with open(r"code\tasks.json", "w") as file:
                dump(data, file, indent=4)
            print("Data saved successfully to task.json")
        except Exception as e:
            print("Error saving data:", e)
        try:
            popup_window.destroy()
        except:
            print("Error(virtual cannot be closed)")
        stop_song()
        print("log data Finished successfully")

    def start_timer():
        global task_start_time,is_Working
        is_Working = True
        task_start_time = str(datetime.today())
        print(task_start_time)
        ttk.Button(bottom_frame, text="end", command=end_timer).grid(column=1,row=2)
        if is_Working:
            root.after(60000,lambda:update_time(Timer,input_minutes))

    def end_timer():
        global is_Working
        is_Working = False
        global task_end_time, commit_common
        task_end_time = str(datetime.today())
        popup_window = tk.Toplevel()
        ttk.Label(popup_window, text="brief Description of Completed task").grid(columnspan=2,row=0,column=0)
        commit_common = ttk.Entry(popup_window)
        commit_common.grid(column=0,row=1)

        ttk.Button(popup_window, text="enter",command=lambda:log_data(TASKS,commit_common,popup_window)).grid(column=1,row=1)
        stop_song()

    def MinToHours(minutes):
        return str(f" {minutes//60}:{minutes%60} ")
    
    def Increment_input_minutes(Value,Timer):
        input_minutes.set(input_minutes.get() + Value)
        Timer = ttk.Label(Pomondero_timer_frame, text=str(MinToHours(input_minutes.get())), font=("Arial", 20)).grid(column=0, row=0, rowspan=2, sticky="ns",padx=5,pady=5)
        
        # Function to play a song
    def play_song():
        # Get song filename (replace with your song path)
        filename = r"References\digital-alarm-2-151919.mp3"
        
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

    # Function to pause the song
    def pause_song():
        pygame.mixer.music.pause()

    # Function to stop the song
    def stop_song():
        pygame.mixer.music.stop()

    def update_time(Timer,input_minutes):
        input_minutes.set( input_minutes.get() - 1)
        Timer = ttk.Label(Pomondero_timer_frame, text=str(MinToHours(input_minutes.get())), font=("Arial", 20)).grid(column=0, row=0, rowspan=2, sticky="ns",padx=5,pady=5)
        if input_minutes.get() > 0:
            root.after(1000,lambda:update_time(Timer,input_minutes))
        else:
            print("Alarm")
            play_song()

    root =  tk.Tk()
    Task_selected = tk.StringVar()

    root.configure(padx=0,pady=0)
    task_start_time = ""
    task_end_time = ""
    input_minutes = tk.IntVar(value=45)


    # define frame --------------------------------
    bottom_frame = ttk.Frame(root, name="time loging").grid(column=0,row=1)
    ttk.OptionMenu(bottom_frame,Task_selected,"main_task",*list(TASKS.keys())).grid(column=0,row=2,padx=5,pady=5)
    ttk.Button(bottom_frame, text="Start", command=start_timer).grid(column=1,row=2)


    # Pomondero --------------------------------
    Pomondero_timer_frame = ttk.Frame(root, name="pomondero_timer").grid(column=0,row=1, sticky="nsew", padx=8,pady=6)
    Timer = ttk.Label(Pomondero_timer_frame, text=str(MinToHours(input_minutes.get())), font=("Arial", 20)).grid(column=0, row=0, rowspan=2, sticky="ns",padx=5,pady=5)
    ttk.Button(text="^", width=3,command=lambda:Increment_input_minutes(5,Timer)).grid(column=1, row=0, sticky="nsew",)
    ttk.Button(text="v", width=3,command=lambda:Increment_input_minutes(-5,Timer)).grid(column=1, row=1, sticky="nsew",)

    root.mainloop()
    #todo Break down larger functions into smaller,
    #todo The ability to add new tasks
    #* Close window automatically when clicked enter
if __name__ == '__main__':
     main()