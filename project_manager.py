from database_schema import create_database
import sqlite3

def insert_new_project(data):
    db = sqlite3.connect("project_manager.db")
    cur = db.cursor()
    cur.execute("""
        INSERT INTO projects(
            project_name,
            project_description
        )
        VALUES(?,?)
    """, 
    data
    )
    db.commit()
    print("Project stored!")
    db.close()

def add_project():
    print("Add new project to database menu")
    project_name = valid_string("project name")
    project_description = valid_string("project description")
    project_data = (project_name, project_description)
    insert_new_project(project_data)

def valid_string(action):
    while True:
        string = input(f"Insert {action}: ").strip()
        if not string:
            print(f"Provided {action} no valid. Please try again")
        else:
            return string

def show_projects():
    db = sqlite3.connect("project_manager.db")
    cur = db.cursor()
    cur.execute("""
        SELECT * FROM projects
    """)
    projects = cur.fetchall()
    for project in projects:
        project_id, project_name, project_description = project
        print(f"""
        {"-"*30}
        Project {project_id} {project_name}
        {project_description}
        {"-"*30}""")
    db.close()

def main():
    # Program goes here
    while True:
        opt = input(f"""
        {'*' * 30}
        1. Add project
        2. Show all projects
        3. Create task
        4. Show project Tasks
        5. Update task
        6. Delete task
        7. Search/Filters tasks
        8. Mark task as complete
        9. Exit
        {'*' * 30}
        Option: """).strip()

        match opt:
            case '1':
                print("Create new project")
                create_database()
                add_project()
            case '2':
                print("Show all projects")
                show_projects()
            case '3':
                print("Create new task")
            case '4':
                print("Show project task")
            case '5':
                print("Update task")
            case '6':
                print("Delete task")
            case '7':
                print("Search/Filter task")
            case '8':
                print("Mark task as complete")
            case '9':
                print("Exit")
                break
            case _:
                print("Option no valid")

if __name__ == '__main__':
    main()


