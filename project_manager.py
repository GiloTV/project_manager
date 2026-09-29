from database_schema import *

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
                print("done")
            case '2':
                print("Show all projects")
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


