from datetime import datetime, date

# Import validation functions
from .validation import validate_due_date, validate_task_description, validate_task_title

# Define tasks list
tasks = []


# Implement add_task function
def add_task(title, description, due_date):
    try:
        validate_task_title(title)
        validate_task_description(description)
        validate_due_date(due_date)

        task = {
            "title": title,
            "description": description,
            "due_date": due_date,
            "completed": False
        }
        tasks.append(task)
        print("Task added successfully!")

    except ValueError as e:
        print(f"Error: {e}")


# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True


# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending_tasks = []

    for task in tasks:
        if not task["completed"]:
            pending_tasks.append(task)

    return pending_tasks


# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    total = len(tasks)

    if total == 0:
        print("No tasks found.")
        return

    completed = sum(1 for task in tasks if task["completed"])

    pending = total - completed
    percentage = (completed / total) * 100

    today = datetime.today().date()
    overdue_tasks = []

    for task in tasks:
        if task["completed"]:
            continue
        due = date.fromisoformat(task["due_date"])
        if due < today:
            overdue_tasks.append(task)

    overdue = len(overdue_tasks)

    print(f"Progress: {completed}/{total} tasks completed ({percentage:.1f}%)")
    print(f"Pending: {pending} | Overdue: {overdue}")
