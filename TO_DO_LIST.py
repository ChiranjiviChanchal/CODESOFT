def add_task(tasks):
  task = input("Enter a new task: ")
  tasks.append(task)
  print("Task added!")

def view_tasks(tasks):
  if not tasks:
    print("No tasks found.")
  else:
    for index, task in enumerate(tasks):
      print(f"{index + 1}. {task}")

def update_task(tasks):
  index = int(input("Enter the task number to update: ")) - 1
  if 0 <= index < len(tasks):
    new_task = input("Enter the new task: ")
    tasks[index] = new_task
    print("Task updated!")
  else:
    print("Invalid task number.")

def main():
  tasks = []
  while True:
    print("\nTo-Do List")
    print("1. Add task")
    print("2. View tasks")
    print("3. Update task")
    print("4. Quit")
    choice = input("Enter your choice: ")
    if choice == '1':
      add_task(tasks)
    elif choice == '2':
      view_tasks(tasks)
    elif choice == '3':
      update_task(tasks)
    elif choice == '4':
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()

