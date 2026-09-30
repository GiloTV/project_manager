import sqlite3
from project_manager import valid_string

def add_project():
    print("Add new project to database menu")
    project_name = valid_string("project name")
    project_description = valid_string("project description")
    project_data = (project_name, project_description)
    insert_new_project(project_data)

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