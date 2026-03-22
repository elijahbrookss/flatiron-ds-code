import re
from datetime import datetime

def validate_task_title(title):
    if not title:
        raise ValueError("Title cannot be empty.")
    if len(title) > 50:
        raise ValueError("Title cannot exceed 50 characters.")
    if not re.match(r'^[A-Za-z0-9 ]+$', title):
        raise ValueError("Title can only contain letters, numbers, and spaces.")

def validate_task_description(description):
    if not description:
        raise ValueError("Description cannot be empty.")
    if len(description) > 200:
        raise ValueError("Description cannot exceed 200 characters.")
    if not re.match(r'^[A-Za-z0-9 .,!?]+$', description):
        raise ValueError("Description contains invalid characters.")

def validate_due_date(due_date):
    if not due_date:
        raise ValueError("Due date cannot be empty.")
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
