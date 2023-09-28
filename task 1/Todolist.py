# Initialize an empty list to store tasks
tasks = []

# Function to display the to-do list
def show_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f"Added: {task}")

# Function to remove a task from the list
def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Removed: {removed_task}")
    else:
        print("Invalid task number.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Show to-do list")
    print("2. Add task")
    print("3. Remove task")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        show_tasks()
    elif choice == '2':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '3':
        index = int(input("Enter the task number to remove: "))
        remove_task(index)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

