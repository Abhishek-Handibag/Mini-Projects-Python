tasks = {}

def add_task(task):
    tasks[task] = "Incomplete"
    print(f"Task '{task}' added.")

def delete_task(task):
    if task in tasks:
        del tasks[task]
        print(f"Task '{task}' deleted.")
    else:
        print(f"Task '{task}' not found.")

def mark_completed(task):
    if task in tasks:
        tasks[task] = "Completed"
        print(f"Task '{task}' marked as completed.")
    else:
        print(f"Task '{task}' not found.")

def show_tasks():
    print("\nTasks:")
    for task, status in tasks.items():
        print(f"- {task} ({status})")

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Mark Task as Completed")
    print("4. Show Tasks")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task_name = input("Enter task name: ")
        add_task(task_name)
    elif choice == "2":
        task_name = input("Enter task name to delete: ")
        delete_task(task_name)
    elif choice == "3":
        task_name = input("Enter task name to mark as completed: ")
        mark_completed(task_name)
    elif choice == "4":
        show_tasks()
    elif choice == "5":
        print("Exiting.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
