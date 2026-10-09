import sqlite3 
from validation import valid_string, valid_number, valid_priority, valid_date, existing_project
from projects import show_projects
from datetime import date

def add_task():
    show_projects()
    project_id = valid_number("project id")
    if existing_project(project_id):
        task_name = valid_string("task name ")
        task_description = valid_string("task description ")
        task_created = str(date.today())
        print("To add the due date add year, month and day automatically will be formatted in YYYY-MM-DD")
        due_date = valid_date()
        status = False
        priority = valid_priority()
        new_task = (task_name, task_description, task_created, due_date, status, priority, project_id)
        print(new_task)
        insert_task(new_task)
    else: 
        print("No project was found. No new task created")

def insert_task(data):
    db = sqlite3.connect("project_manager.db")
    db.execute("PRAGMA foreign_keys = ON")
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

def show_single_project_tasks():
    db = sqlite3.connect("project_manager.db")
    cur = db.cursor()
    while True:
        project_id = valid_number("project id")
        if existing_project(project_id):
            cur.execute("""
                SELECT
                    projects.project_id,
                    projects.project_name,
                    tasks.task_id,
                    tasks.task_name,
                    tasks.task_description,
                    tasks.due_date,
                    tasks.status,
                    tasks.priority
                FROM projects
                INNER JOIN tasks 
                ON projects.project_id = tasks.project_id
                WHERE projects.project_id = ?
            """,(project_id,))
            tasks = cur.fetchall()
            if tasks:
                for task in tasks:
                    projct_id, project_name, task_id, task_name, task_description, due_date, task_status, priority = task
                    print(f"""
                        {'-'*30}
                        project {projct_id}: {project_name}
                        task {task_id}: {task_name}
                        {'-'*30}
                        description: {task_description}
                        due: {due_date}
                        status: {"Completed!" if task_status > '0' else "Pending..."}
                        priority: {priority}
                        {'-'*30}""")
            elif not tasks:
                print(f"No tasks yet for {project_id}!")
            break
        else: 
            print("Please select a valid project ID")
    db.close()

def show_all_projects_tasks():
    db = sqlite3.connect("project_manager.db")
    cur = db.cursor()
    cur.execute("""
        SELECT
            projects.project_id,
            projects.project_name,
            tasks.task_id,
            tasks.task_name,
            tasks.task_description,
            tasks.due_date,
            tasks.status,
            tasks.priority
        FROM projects
        LEFT JOIN tasks 
        ON projects.project_id = tasks.project_id
        ORDER BY projects.project_id
    """)
    tasks = cur.fetchall()
    if tasks:
        for task in tasks:
            projct_id, project_name, task_id, task_name, task_description, due_date, task_status, priority = task
            if task_name:
                print(f"""
                    {'-'*30}
                    project {projct_id}: {project_name}
                    task {task_id}: {task_name}
                    {'-'*30}
                    description: {task_description}
                    due: {due_date}
                    status: {"Pending..." if '0' in task_status else "Completed"}
                    priority: {priority}
                    {'-'*30}""")
            else:
                print(f"""
                    {'-'*30}
                    project {projct_id}: {project_name}
                    No tasks yet!
                    {'-'*30}""")
    db.close()

def update_name(project, task):
    while True:
        new_task_name = input(f"Please type the new task name for '{task[1]}' Or if you like to cancel type 'c' | 'cancel'\n -> ").strip()
        if new_task_name in ["c", "cancel", "C", "CANCEL",]:
            print("Action cancelled")
            break
        elif new_task_name:
            db = sqlite3.connect("project_manager.db")
            cur = db.cursor()
            cur.execute("""
                UPDATE tasks 
                SET task_name = ? 
                WHERE task_id = ? and project_id = ?
            """, (new_task_name, task[0], project))
            db.commit()
            print("Task name updated")
            db.close()
            break     
        else:
            print("Invalid name. No empty values allowed")

def update_description(project, task):
    while True:
        new_task_description = input(f"Please type the new description for {task[1]} Or if you like to cancel type 'c' | 'cancel'\n -> ").strip()
        if new_task_description in ["c", "cancel", "C", "CANCEL", "n", "no"]:
            print("Action cancelled")
            break
        elif new_task_description:
            db = sqlite3.connect("project_manager.db")
            cur = db.cursor()
            cur.execute("""
                UPDATE tasks 
                SET task_description = ?
                WHERE task_id = ? and project_id = ? 
            """,(new_task_description, task[0], project))
            db.commit()
            print("Task description updated")
            db.close()  
            break
        else:
            print("Invalid name. No empty values allowed")

def update_due_date(project, task):
    print(f"Please type the new date for {task[1]}")
    while True:
        new_task_due_date = valid_date()
        if new_task_due_date:
            db = sqlite3.connect("project_manager.db")
            cur = db.cursor()
            cur.execute("""
                    UPDATE tasks 
                    SET due_date = ?
                    WHERE task_id = ? and project_id = ? 
                """,(new_task_due_date, task[0], project))
            db.commit()
            print("Task due date updated")
            db.close()
            break 
        else: 
            confirmation = input("No changes were made. Try again? 'Y' | 'N'\n -> ").strip().lower()
            if confirmation in ["y", "yes"]:
                print("Re type date please")
            else:
                print("Returning to previous menu")
                break
            
def update_status(project, task):
    db = sqlite3.connect("project_manager.db")
    cur = db.cursor()
    cur.execute("""
    SELECT status from tasks
    WHERE task_id = ? and project_id = ?
    """, (task[0], project))
    current_status = cur.fetchone()
    print(current_status)
    cur.execute("""
            UPDATE tasks 
            SET status = ?
            WHERE task_id = ? and project_id = ? 
        """,("1" if current_status[0] == "0" else "0", task[0], project))
    db.commit()
    print("Task status changed")
    db.close()


def update_priority(project, task):
    new_task_priority = valid_priority()
    db = sqlite3.connect("project_manager.db")
    cur = db.cursor()
    cur.execute("""
                UPDATE tasks 
                SET priority = ?
                WHERE task_id = ? and project_id = ? 
            """,(new_task_priority, task[0], project))
    db.commit()
    print(f"Task priority changed to {new_task_priority}")
    db.close()

def delete_task(project, task):
    db = sqlite3.connect("project_manager.db")
    cur = db.cursor()
    cur.execute("""
        DELETE FROM tasks
        WHERE task_id = ? AND project_id = ?
    """,(task, project))
    db.commit()
    print(f"Task {task} from project {project} deleted successfully!")
    db.close()

def filter_by_priority(priority):
    db = sqlite3.connect("project_manager.db")
    cur = db.cursor()
    cur.execute("""
        SELECT * FROM tasks
        WHERE priority = ?
    """, (priority,))
    task = cur.fetchall()
    print(task)