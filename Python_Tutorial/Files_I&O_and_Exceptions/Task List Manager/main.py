import os

def add_task(task_list, task):
    task_list.append(task)
    print(f"Task '{task}' added to the list.")

def remove_task(task_list, task):
    try:
        task_list.remove(task)
        print(f"Task '{task}' removed from the list.")
    except ValueError:
        print(f"Error: Task '{task}' not found in the list.")

def view_tasks(task_list):
    if task_list:
        print("\nCurrent Task List:")
        for i, task in enumerate(task_list, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks in the list.")

def save_tasks(filename, task_list):
    try:
        with open(filename, 'w') as file:
            for task in task_list:
                file.write(f"{task}\n")
        print("Tasks successfully saved!")
    except IOError as e:
        print(f"Error while saving tasks: {e}")

def load_tasks(filename):
    task_list = []
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                task_list = [line.strip() for line in file.readlines()]
            print("Tasks loaded successfully!")
        except IOError as e:
            print(f"Error while loading tasks: {e}")
    return task_list

def main():
    filename = "tasks.txt"
    task_list = load_tasks(filename)

    while True:
        print("\nTask List Manager")
        print("1. Add a Task")
        print("2. Remove a Task")
        print("3. View Task List")
        print("4. Save Tasks")
        print("5. Exit")

        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                task = input("Enter the task: ")
                add_task(task_list, task)
            elif choice == 2:
                view_tasks(task_list)
                task_to_remove = input("Enter the task to remove: ")
                remove_task(task_list, task_to_remove)
            elif choice == 3:
                view_tasks(task_list)
            elif choice == 4:
                save_tasks(filename, task_list)
            elif choice == 5:
                print("Exiting the program.")
                save_tasks(filename, task_list)
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the menu option.")

if __name__ == "__main__":
    main()
