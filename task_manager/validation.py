from datetime import datetime

def validate_task_title(title):
    if not title or not isinstance(title, str) or title.strip() == "":
        raise ValueError("Invalid title. Title cannot be empty.")
    return True

def validate_task_description(description):
    if not description or not isinstance(description, str) or description.strip() == "":
        raise ValueError("Invalid description. Description cannot be empty.")
    if len(description) > 500:
        raise ValueError("Invalid description. Description cannot exceed 500 characters.")
    return True

def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError("Invalid due date. Please use the format YYYY-MM-DD.")
