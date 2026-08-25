import json
import os
file_name = "tasks.json"
def load_tasks():
    if os.path.exists(file_name):
        try:
            with open(file_name, "r") as file:
                return json.load(file)
        except:
            return []
    return []
def save_tasks(tasks):
    with open(file_name, "w") as file:
        json.dump(tasks, file, indent=4)
def add_task(tasks):
    task_name = input("Enter task: ")
    if task_name == "":
        print("Task cannot be empty!")
        return
    print("\nChoose Priority:")
    print("1. Low")
    print("2. Medium")
    print("3. High")
    choice = input("Enter choice: ")
    if choice == "1":
        priority = "Low"
    elif choice == "3":
        priority = "High"
    else:
        priority = "Medium"
    task = {
        "title": task_name,
        "priority": priority,
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")
def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return
    print("---- YOUR TASKS ----")
    for i in range(len(tasks)):
        task = tasks[i]
        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"
        print(
            i + 1,
            task["title"],
            "| Priority:", task["priority"],
            "|", status
        )
def complete_task(tasks):
    view_tasks(tasks)
    if len(tasks) == 0:
        return
    try:
        number = int(input("\nEnter task number: "))
        if number >= 1 and number <= len(tasks):
            tasks[number - 1]["completed"] = True
            save_tasks(tasks)
            print("Task completed!")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a number.")
def delete_task(tasks):
    view_tasks(tasks)
    if len(tasks) == 0:
        return
    try:
        number = int(input("\nEnter task number to delete: "))
        if number >= 1 and number <= len(tasks):
            deleted_task = tasks.pop(number - 1)
            save_tasks(tasks)
            print("Deleted:", deleted_task["title"])
        else:
            print("Invalid task number.")
    except:
        print("Please enter a number.")
def search_task(tasks):
    keyword = input("Enter task name to search: ").lower()
    found = False
    for i in range(len(tasks)):
        task = tasks[i]
        if keyword in task["title"].lower():
            if task["completed"]:
                status = "Completed"
            else:
                status = "Pending"
            print(
                i + 1,
                task["title"],
                "| Priority:", task["priority"],
                "|", status
            )
            found = True
    if found == False:
        print("No task found.")
def show_statistics(tasks):
    total = len(tasks)
    completed = 0
    for task in tasks:
        if task["completed"]:
            completed = completed + 1
    pending = total - completed
    print("---- STATISTICS ---")
    print("Total Tasks:", total)
    print("Completed Tasks:", completed)
    print("Pending Tasks:", pending)
    if total > 0:
        percentage = (completed / total) * 100
        print("Completion Rate:", percentage, "%")
def main():
    tasks = load_tasks()
    print("---- To DO Manager ----")
    while True:
        print("---- MENU ----")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Search Task")
        print("6. Statistics")
        print("7. Exit")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            search_task(tasks)
        elif choice == "6":
            show_statistics(tasks)
        elif choice == "7":
            save_tasks(tasks)
            print("Tasks saved!")
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
main()

