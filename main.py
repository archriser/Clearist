from datetime import datetime

# A simple list to store tasks
tasks = []

def show_all_tasks():
    """Display all tasks or a message if no tasks are available."""
    if not tasks:
        print("No tasks available.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_new_task():
    """Add a new task to the list."""
    task = input("Enter the task description: ")
    tasks.append(task)
    print("Task added successfully!")

def delete_task():
    """Delete a task based on user input."""
    show_all_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' deleted.")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

def show_today():
    """Display today's date."""
    today = datetime.now().strftime("%A, %d %B %Y")
    print(f"Today is {today}.")

def about_dev():
    """Display information about the developer."""
    print("Developed by Md. Tasdik Bin Yousuf Sabik.")
    print("Student of Mechanical Engineering at Shahjalal University of Science and Technology.")
    print("Enjoy organizing your tasks with Clyde!")

def main_menu():
    """Display the main menu and handle user choices."""
    while True:
        print("\nWelcome to Clyde - Your Command-Line To-Do App")
        print("1. Show All Tasks")
        print("2. Add New Task")
        print("3. Delete a Task")
        print("4. Show What is Today")
        print("5. About the Developer")
        print("6. Exit")
        
        choice = input("Please select an option (1-6): ")
        
        if choice == '1':
            show_all_tasks()
        elif choice == '2':
            add_new_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            show_today()
        elif choice == '5':
            about_dev()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
