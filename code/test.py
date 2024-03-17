import json

with open(r"code\tasks.json", "r") as file:
    TASKS = json.load(file)
    print (TASKS)