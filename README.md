# 📝 Command-Line To-Do List Manager

A feature-rich command-line to-do list manager built in Python with priority levels, due dates, and task filtering capabilities.

## ✨ Features

- **Task Management**: Add, edit, delete, and mark tasks as complete
- **Priority Levels**: Organize tasks with low, medium, and high priority levels
- **Due Dates**: Set optional due dates for tasks (YYYY-MM-DD format)
- **Smart Filtering**: View tasks by status (all, completed, pending, due soon)
- **Persistent Storage**: Tasks are automatically saved to and loaded from a JSON file
- **User-Friendly Interface**: Clean, emoji-enhanced command-line interface
- **Smart Sorting**: Tasks are automatically sorted by priority (high → medium → low)

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- No additional dependencies required (uses only Python standard library)

### Installation

1. Clone or download the project files
2. Ensure you have `todo_manager.py` in your project directory
3. Run the program:

```bash
python todo_manager.py
```

## 📋 Usage

When you run the program, you'll see a main menu with the following options:

### Main Menu Options

1. **Add Task** - Create a new task with description, optional due date, and priority level
2. **View All Tasks** - Display all tasks sorted by priority
3. **View Completed Tasks** - Show only completed tasks
4. **View Pending Tasks** - Show only incomplete tasks
5. **View Tasks Due Soon** - Display tasks due within the next 3 days
6. **Mark Task as Completed** - Mark a pending task as done
7. **Edit a Task** - Modify task description, due date, or priority
8. **Delete a Task** - Remove a task from the list
9. **Exit** - Save tasks and quit the program

### Adding Tasks

When adding a task, you'll be prompted for:
- **Description**: What needs to be done
- **Due Date** (optional): Date in YYYY-MM-DD format (e.g., 2025-12-31)
- **Priority**: Choose from low, medium, or high (defaults to medium if invalid)

### Task Display Format

Tasks are displayed with the following information:
```
1. Task description (Due: YYYY-MM-DD) [✅/❌] Priority: high/medium/low
```

- ✅ indicates completed tasks
- ❌ indicates pending tasks
- Tasks are automatically sorted by priority (high priority shown first)

## 💾 Data Storage

- Tasks are stored in `tasks.json` in the same directory as the script
- Data is automatically loaded when the program starts
- Data is saved when you exit the program (option 9)
- You can manually save at any time by selecting "Exit" and then restarting

## 🔧 Technical Details

### File Structure
```
Command-Line To-Do List Manager/
│
├── todo_manager.py    # Main application file
├── tasks.json         # Task data storage (created automatically)
└── README.md          # This file
```

### Key Functions

- `load_tasks()`: Loads tasks from JSON file
- `save_tasks(tasks)`: Saves tasks to JSON file
- `add_task(tasks)`: Adds a new task
- `view_tasks(tasks, filter_type)`: Displays filtered task list
- `mark_complete(tasks)`: Marks tasks as completed
- `edit_task(tasks)`: Edits existing tasks
- `delete_task(tasks)`: Removes tasks

### Task Data Structure

Each task is stored as a dictionary with the following structure:
```python
{
    "description": "Task description",
    "due_date": "2025-12-31",  # Optional, can be null
    "completed": false,        # Boolean status
    "priority": "high"         # "low", "medium", or "high"
}
```

## 🎯 Usage Examples

### Example 1: Adding a High-Priority Task
```
Enter task description: Complete project presentation
Enter due date (YYYY-MM-DD) or leave blank: 2025-08-01
Priority (low/medium/high): high
✅ Task added!
```

### Example 2: Viewing Tasks Due Soon
Tasks due within the next 3 days will be displayed when selecting option 5.

## 🛠️ Customization

You can easily customize the application by modifying:

- **Due Soon Range**: Change the 3-day threshold in the `view_tasks()` function
- **Priority Levels**: Add more priority levels by modifying the `priority_order` dictionary
- **File Location**: Change the `FILENAME` constant to store tasks elsewhere
- **Date Format**: Modify date parsing in the `view_tasks()` function

## 🐛 Error Handling

The application includes error handling for:
- Missing task files (creates new empty list)
- Invalid date formats (gracefully ignored)
- Invalid priority levels (defaults to "medium")
- Invalid menu choices (prompts for retry)
- Index out of range errors for task selection

## 📈 Future Enhancements

Potential features that could be added:
- Task categories/tags
- Search functionality
- Task notes/details
- Recurring tasks
- Export to different formats
- Multiple priority sorting options
- Task statistics and reports

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!

## 📄 License

This project is open source and available under the MIT License.

---

*Built with Python 3 - Simple, effective task management from the command line!*
