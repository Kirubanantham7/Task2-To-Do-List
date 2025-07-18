import os
from datetime import datetime

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

TASK_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# View tasks
def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    print()

# Add a task
def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task '{task}' added.\n")
    else:
        print("Task cannot be empty.\n")

# Remove a task
def remove_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the number of the task to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"Task '{removed}' removed.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Main loop
def main():
    tasks = load_tasks()
    while True:
        clear_screen()
        print("╔════════════════════════════════════════════╗")
        print('║            TO-DO LIST MENU                 ║')
        print("╠════════════════════════════════════════════╣")
        print('║ 1. View tasks                              ║')
        print('║ 2. Add task                                ║')
        print('║ 3. Remove task                             ║')
        print('║ 4. Exit                                    ║')
        print("╚════════════════════════════════════════════╝")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            view_tasks(tasks)
            input("Press Enter to continue...")
            continue
        elif choice == "2":
            add_task(tasks)
            input("Press Enter to continue...")
            continue
        elif choice == "3":
            remove_task(tasks)
            input("Press Enter to continue...")
            continue
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.\n")
            input("Press Enter to continue...")
            continue

if __name__ == "__main__":
    main()
