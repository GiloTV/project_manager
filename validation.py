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
                print("Select a valid priority!")

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
        project_id = valid_number("project id")
        if project_id in id_list:
            cur.execute("""
                SELECT project_name from projects WHERE project_id = ?
            """, (project_id,))
            project_name = cur.fetchone()
            print(f"Project found! {project_name[0]}")
            db.close()
            return project_id
        else:
            print("No project found with that ID, try again!")

def valid_task_id():
    db = sqlite3.connect("project_manager.db")
    cur = db.cursor()
    cur.execute("""
        SELECT task_id from tasks
    """)
    tasks_id = cur.fetchall()
    id_list = []
    for existing_id in tasks_id:
        id_list.append(existing_id[0])

    while True:
        task_id = valid_number("task id")
        if task_id in id_list:
            cur.execute("""
                SELECT task_id, task_name from tasks WHERE task_id = ?
            """, (task_id,))
            task = cur.fetchone()
            print(f"Task found! {task[1]}")
            db.close()
            return task
        #Maybe put here a cancelation
        else:
            print("No task found with that ID, try again!")

def valid_date():
    while True:
        year = valid_number("year")
        month = valid_number("month")
        day = valid_number("day")
        try:
            task_due_date = datetime.date(year,month, day)
            return str(task_due_date)
        except ValueError as va:
            print("Value Error", va)

def fast_travel(action):
    while True:
        confirmation = input(f"Would you like to continue {action}? Y | N\n -> ").strip().lower()
        if confirmation in ["y", "yes"]:
            return False
        if confirmation in ["n", "no"]:
            return True
        else:
            print("Select a valid option")

