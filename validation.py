import sqlite3
import datetime

def valid_string(action):
    while True:
        string = input(f"Insert {action}: ").strip()
        if not string:
            print(f"Provided {action} no valid. Please try again")
        else:
            return string

def valid_number(action):
    while True:
        number = input(f"Insert {action}: ").strip()
        try:
            number = int(number)
            if number > 0:
                return number
            else:
                print(f"{action} must be higher than 0")
        except ValueError:
            print("Not a number")

def valid_priority():
    while True:
        priority = input("""Select priority
            1.- Low
            2.- Medium
            3.- High
        """)
        match priority:
            case '1':
                priority = 'Low'
                return priority
            case '2':
                priority = 'Medium'
                return priority
            case '3':
                priority = 'High'
                return priority
            case _:
                priority("Select a valid priority!")

def valid_project_id():
    db = sqlite3.connect("project_manager.db")
    cur = db.cursor()
    cur.execute("""
        SELECT project_id from projects
    """)
    projects_id = cur.fetchall()
    id_list = []
    for existing_id in projects_id:
        id_list.append(existing_id[0])

    while True:
        print("Which project will have a task added: ")
        project_id = valid_number("project id")
        if project_id in id_list:
            cur.execute("""
                SELECT project_name from projects WHERE project_id = ?
            """, (project_id,))
            project_name = cur.fetchone()
            print(f"New task will be added to project {project_name[0]}")
            db.close()
            return project_id
        else:
            print("No project found with that ID, try again!")

def valid_date():
    while True:
        year = valid_number("year")
        month = valid_number("month")
        day = valid_number("day")
        try:
            task_due_date = datetime.date(year,month, day)
            print("value: ", task_due_date)
            print("type: ", type(str(task_due_date)))
            return str(task_due_date)
        except ValueError as va:
            print("Value Error", va)
