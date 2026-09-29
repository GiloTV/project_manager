import sqlite3

# How do I identify one exact project or task? → Give each table its own primary key.
# How does a task tell me which project owns it? → Put the project’s ID in tasks as a foreign key.

def create_database():
    db = sqlite3.connect("project_manager.db")
    db.execute("PRAGMA foreign_keys = ON")
    cur = db.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            project_id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_name TEXT NOT NULL,
            project_description TEXT NOT NULL
        )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_name TEXT NOT NULL,
        task_description TEXT NOT NULL,
        date_created TEXT NOT NULL,
        due_date TEXT NOT NULL,
        status TEXT NOT NULL,
        priority TEXT,
        project_id INTEGER NOT NULL,

        FOREIGN KEY (project_id) REFERENCES projects(project_id)
    )
""")

    db.commit()
    db.close()