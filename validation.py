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

def existing_project(project_id):
    db = sqlite3.connect("project_manager.db")
    cur = db.cursor()
    cur.execute("""
        SELECT * from projects 
        WHERE project_id = ?
    """, (project_id,))
    res = cur.fetchone()
    db.close()
    return res

def existing_task(project_id, task_id):
    db = sqlite3.connect("project_manager.db")
    cur = db.cursor()
    cur.execute("""
        SELECT * from tasks 
        WHERE task_id = ? AND project_id = ?
    """, (task_id, project_id))
    res = cur.fetchone()
    db.close()
    return res 


def valid_date():
    while True:
        try:
            year = valid_number("year")
            month = valid_number("month")
            day = valid_number("day")
            
            return datetime.date(year, month, day).isoformat()
        except ValueError as va:
            print("Value Error", va)
            
def fast_travel(action):
    while True:
        confirmation = input(f"Would you like to continue {action}? Y | N\n -> ").strip().lower()
        if confirmation in ["y", "yes"]:
            return True
        if confirmation in ["n", "no"]:
            return False
        else:
            print("Select a valid option")

