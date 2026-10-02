import sqlite3 
from validation import valid_string, valid_number, valid_priority, valid_project_id, valid_date
from projects import show_projects
from datetime import date

def add_task():
    show_projects()
    project_id = valid_project_id()
    task_name = valid_string("task name ")
    task_description = valid_string("task description ")
    task_created = str(date.today())
    print("Insert the due date of this task in the following format YYYY-MM-")
    due_date = valid_date()
    status = False
    priority = valid_priority()
    new_task = (task_name, task_description, task_created, due_date, status, priority, project_id)
    print(new_task)
    insert_task(new_task)

def insert_task(data):
    db = sqlite3.connect("project_manager.db")
    cur = db.cursor()
    cur.execute("""
        INSERT INTO tasks (
            task_name,
            task_description,
            date_created,
            due_date,
            status,
            priority,
            project_id
        )
        VALUES(?,?,?,?,?,?,?)
    """, data)
    db.commit()
    print("Data saved!")
    db.close()