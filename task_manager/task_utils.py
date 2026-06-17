from datetime import datetime
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

tasks = []

def add_task(title, description, due_date):
    try:
        validate_task_title(title)
        validate_task_description(description)
        validate_due_date(due_date)
    except ValueError as e:
        print(e)
        return
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

def mark_task_as_complete(index, tasks=tasks):
    if index < 0 or index >= len(tasks):
        print("Invalid task index.")
        return
    tasks[index]["completed"] = True
    print("Task marked as complete!")

def view_pending_tasks(tasks=tasks):
    pending = [task for task in tasks if not task["completed"]]
    if not pending:
        print("No pending tasks.")
    else:
        print("\nPending Tasks:")
        for i, task in enumerate(pending):
            print(f"{i + 1}. [{task['due_date']}] {task['title']} - {task['description']}")

def calculate_progress(tasks=tasks):
    if not tasks:
        progress = 0
    else:
        completed = sum(1 for task in tasks if task["completed"])
        progress = (completed / len(tasks)) * 100
    return progress
