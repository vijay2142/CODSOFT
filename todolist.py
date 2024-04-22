class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_index):
        del self.tasks[task_index]

    def display_tasks(self):
        if self.tasks:
            print("Tasks:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")
        else:
            print("No tasks.")

    def update_task(self, task_index, new_task):
        self.tasks[task_index] = new_task


def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add task")
        print("2. Remove task")
        print("3. Display tasks")
        print("4. Update task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task_index = int(input("Enter the index of the task to remove: ")) - 1
            todo_list.remove_task(task_index)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            task_index = int(input("Enter the index of the task to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_index, new_task)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
