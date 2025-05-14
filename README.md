# ✅ CLI To-Do List App (Python)

A simple **Command Line Interface (CLI)** To-Do List app made with Python.  
It helps you **add, view, complete, and delete tasks** directly from the terminal.

---

## 📌 Features

- 📋 View all tasks with status (✅ Done / ❌ Not Done)
- ➕ Add a new task
- ☑️ Mark a task as completed
- ❌ Delete a task
- 🔁 Repeat menu until you choose to exit

---

# Requirements

- Python 3.x
- No external libraries are required; the project uses only built-in Python features.


## 🏗️ How It Works

Each task is saved as a **dictionary** with two values:
- `"name"`: the task name
- `"done"`: whether the task is completed (`True` or `False`)

All tasks are stored in a Python list called `tasks`.

---

## 🧪 Sample Output

```bash
======= TO-DO LIST MENU =======
1. View tasks
2. Add a new task
3. Mark a task as completed
4. Delete a task
5. Exit the app
================================
Enter your choice (1-5): 2
Enter a task name: Study Python
Task 'Study Python' added successfully!
