from datetime import datetime

def validate_task_title(title):
    if not title or not isinstance(title, str) or title.strip() == "":
        print("Invalid title. Title cannot be empty.")
        return False
    return True

def validate_task_description(description):
    if not description or not isinstance(description, str) or description.strip() == "":
        print("Invalid description. Description cannot be empty.")
        return False
    return True

def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        print("Invalid due date. Please use the format YYYY-MM-DD.")
        return False
