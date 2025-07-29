import json
from datetime import datetime, timedelta

FILENAME = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)

# Add a new task
def add_task(tasks):
    desc = input("Enter task description: ")
    due = input("Enter due date (YYYY-MM-DD) or leave blank: ")
    priority = input("Priority (low/medium/high): ").lower()
    if priority not in ["low", "medium", "high"]:
        priority = "medium"
    task = {
        "description": desc,
        "due_date": due if due else None,
        "completed": False,
        "priority": priority
    }
    tasks.append(task)
    print("✅ Task added!")

# View tasks (with optional filter)
def view_tasks(tasks, filter_type="all"):
    print("\n--- Task List ---")
    today = datetime.now().date()

    # Sort by priority (high > medium > low)
    priority_order = {"high": 0, "medium": 1, "low": 2}
    tasks_sorted = sorted(tasks, key=lambda x: priority_order.get(x.get("priority", "medium")))

    for i, task in enumerate(tasks_sorted):
        due = task['due_date']
        due_str = f"(Due: {due})" if due else ""
        status = "✅" if task["completed"] else "❌"
        show = False

        if filter_type == "all":
            show = True
        elif filter_type == "completed" and task["completed"]:
            show = True
        elif filter_type == "pending" and not task["completed"]:
            show = True
        elif filter_type == "due_soon":
            if due:
                try:
                    due_date = datetime.strptime(due, "%Y-%m-%d").date()
                    if 0 <= (due_date - today).days <= 3:
                        show = True
                except ValueError:
                    pass

        if show:
            print(f"{i + 1}. {task['description']} {due_str} [{status}] Priority: {task['priority']}")
    print()

# Mark a task as complete
def mark_complete(tasks):
    view_tasks(tasks, "pending")
    idx = int(input("Enter task number to mark complete: ")) - 1
    if 0 <= idx < len(tasks):
        tasks[idx]["completed"] = True
        print("✅ Task marked as complete.")

# Edit a task
def edit_task(tasks):
    view_tasks(tasks)
    idx = int(input("Enter task number to edit: ")) - 1
    if 0 <= idx < len(tasks):
        desc = input("New description (leave blank to keep current): ")
        due = input("New due date (YYYY-MM-DD) or leave blank: ")
        prio = input("New priority (low/medium/high) or leave blank: ").lower()

        if desc:
            tasks[idx]["description"] = desc
        if due:
            tasks[idx]["due_date"] = due
        if prio in ["low", "medium", "high"]:
            tasks[idx]["priority"] = prio
        print("✏️ Task updated.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    idx = int(input("Enter task number to delete: ")) - 1
    if 0 <= idx < len(tasks):
        removed = tasks.pop(idx)
        print(f"🗑️ Deleted task: {removed['description']}")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("""
--- 📝 To-Do List Manager ---
1. Add Task
2. View All Tasks
3. View Completed Tasks
4. View Pending Tasks
5. View Tasks Due Soon
6. Mark Task as Completed
7. Edit a Task
8. Delete a Task
9. Exit
""")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks, "all")
        elif choice == "3":
            view_tasks(tasks, "completed")
        elif choice == "4":
            view_tasks(tasks, "pending")
        elif choice == "5":
            view_tasks(tasks, "due_soon")
        elif choice == "6":
            mark_complete(tasks)
        elif choice == "7":
            edit_task(tasks)
        elif choice == "8":
            delete_task(tasks)
        elif choice == "9":
            save_tasks(tasks)
            print("💾 Tasks saved. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    main()
