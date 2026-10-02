from database_schema import create_database
from projects import add_project, show_projects
from tasks import add_task, show_single_project_tasks, show_all_projects_tasks

def main():
    # Program goes here
    create_database()
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
                add_project()
            case '2':
                print("Show all projects")
                show_projects()
            case '3':
                print("Create new task")
                add_task()
            case '4':
                print("Show project task")
                while True:
                    show_project_tasks_opt = input(f"""
                        {'*' * 30}
                        1. Show single project tasks
                        2. Show all projects all tasks
                        3. Exit
                        {'*' * 30}
                        Option: """).strip()
                    match show_project_tasks_opt:
                        case '1':
                            show_single_project_tasks()
                            break
                        case '2':
                            show_all_projects_tasks()
                            break
                        case '3':
                            print("Returning to main menu...")
                        case _:
                            print("Select a valid option")
                            

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


