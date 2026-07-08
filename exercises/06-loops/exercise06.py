# Exercise 6: Enumerate — To-Do List
# Use enumerate() to display numbered tasks, remove completed ones.

tasks = ["Buy groceries", "Finish homework", "Call mom"]


def print_tasks():
    print("Your Tasks:")
    if len(tasks):
        for i, task in enumerate(tasks):
            print(f"{i}. {task:8}")
    else:
        print("All Tasks completed.")


print_tasks()

while True:
    reply = input("Which task is complete? (0 to quit): ").strip()
    if reply == "0":
        print("Goodbye!")
        break
    else:
        tasks.remove(reply)
        print_tasks()
