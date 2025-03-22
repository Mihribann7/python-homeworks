import json
import csv

try:
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
        if not tasks:
            print("The file is empty")
            tasks = []
except (FileNotFoundError, json.JSONDecodeError):
    print("Error")
    tasks = []

if tasks:
    print("ID; Task; Completed; Priority")
    for task in tasks:
        print(f"{task['id']}: {task['task']},{task['completed']},{task['priority']}")

if tasks:
    total_tasks = len(tasks)
    completed_tasks = sum(task['completed'] for task in tasks)
    pending_tasks = total_tasks - completed_tasks
    average_priority = round(sum(task['priority'] for task in tasks) / total_tasks, 1)

    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {average_priority}")

if tasks:
    with open('tasks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])

else:
    print("No tasks")
