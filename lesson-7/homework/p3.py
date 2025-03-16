import json
import csv

class Task:
    def __init__(self, task_id, title, description, due_date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"


class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.extension = filename.split('.')[-1]

    def save(self, tasks):
        if self.extension == 'csv':
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Task ID', 'Title', 'Description', 'Due Date', 'Status'])
                for task in tasks:
                    writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])

        elif self.extension == 'json':
            data = [{'task_id': task.task_id, 'title': task.title, 'description': task.description,
                     'due_date': task.due_date, 'status': task.status} for task in tasks]
            with open(self.filename, 'w') as file:
                json.dump(data, file, indent=4)
        else:
            raise ValueError("Unsupported file format")

    def load(self):
        tasks = []
        if self.extension == 'csv':
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    tasks.append(Task(row['Task ID'], row['Title'], row['Description'], row['Due Date'], row['Status']))

        elif self.extension == 'json':
            with open(self.filename, 'r') as file:
                data = json.load(file)
                for item in data:
                    tasks.append(Task(item['task_id'], item['title'], item['description'], item['due_date'], item['status']))
        else:
            raise ValueError("Unsupported file format")

        return tasks


class ToDoApp:
    def __init__(self, filename):
        self.tasks = []
        self.file_handler = FileHandler(filename)

    def add_task(self):
        task_id = input("Enter Task ID: ")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD): ")

        status = input("Enter Status (In Progress/Completed): ")
        while status not in ["In Progress", "Completed"]:
            print("Status must be 'In Progress' or 'Completed'!")
            status = input("Enter Status (In Progress/Completed): ")

        self.tasks.append(Task(task_id, title, description, due_date, status))
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)

    def update_task(self):
        task_id = input("Enter Task ID to update: ")
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = input("Enter new title (leave empty to keep current): ") or task.title
                task.description = input("Enter new description (leave empty to keep current): ") or task.description
                task.due_date = input("Enter new due date (leave empty to keep current): ") or task.due_date
                new_status = input("Enter new status (In Progress/Completed): ") or task.status
                while new_status not in ["In Progress", "Completed"]:
                    print("Status must be 'In Progress' or 'Completed'!")
                    new_status = input("Enter new status (In Progress/Completed): ")
                task.status = new_status
                print("Task updated successfully!")
                return
        print("Task not found!")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully!")
                return
        print("Task not found!")

    def filter_tasks_by_status(self):
        status = input("Enter status to filter (In Progress/Completed): ")
        if status not in ["In Progress", "Completed"]:
            print("Invalid status!")
            return

        filtered_tasks = [task for task in self.tasks if task.status == status]
        if not filtered_tasks:
            print("No tasks found with that status.")
        else:
            for task in filtered_tasks:
                print(task)

    def save_tasks(self):
        self.file_handler.save(self.tasks)
        print("Tasks saved successfully!")

    def load_tasks(self):
        self.tasks = self.file_handler.load()
        print("Tasks loaded successfully!")

    def run(self):
        while True:
            print("""
Welcome to the To-Do Application!
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Load tasks
8. Exit
""")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.filter_tasks_by_status()
            elif choice == "6":
                self.save_tasks()
            elif choice == "7":
                self.load_tasks()
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    filename = input("Enter filename (e.g., tasks.json or tasks.csv): ")
    app = ToDoApp(filename)
    app.run()
