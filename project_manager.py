from database_schema import create_database
from projects import add_project, show_projects
import tasks
from validation import fast_travel, valid_project_id, valid_task_id

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
        8. Exit
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
                tasks.add_task()
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
                            tasks.show_single_project_tasks()
                            break
                        case '2':
                            tasks.show_all_projects_tasks()
                            break
                        case '3':
                            print("Returning to main menu...")
                        case _:
                            print("Select a valid option")
            case '5':
                    print("Update task menu.")
                    project_id = valid_project_id()
                    task = valid_task_id()
                    print("Project", project_id)
                    print("Task", task)
                    if project_id and task:
                        while True:
                            update_task_opt = input(f"""
                                {'*' * 30}
                                1. Name
                                2. Description
                                3. Due Date
                                4. Status
                                5. Priority
                                6. Back
                                {'*' * 30}
                                Option: """).strip()
                            match update_task_opt:
                                case '1':
                                    print("Update task selected!")  
                                    tasks.update_name(project_id, task)
                                    if not fast_travel("updating tasks"):
                                        break                  
                                case '2':
                                    print("Update description") 
                                    tasks.update_description(project_id, task)
                                    if not fast_travel("updating tasks"):
                                        break  
                                case '3':
                                    print("Update due date") 
                                    tasks.update_due_date(project_id, task)
                                    if not fast_travel("updating tasks"):
                                        break 
                                case '4':
                                    print("Update status")
                                    tasks.update_status(project_id, task)
                                    if not fast_travel("updating tasks"):
                                        break   
                                case '5':
                                    print("Update priority")
                                    tasks.update_priority(project_id, task)
                                    if not fast_travel("updating tasks"):
                                        break 
                                case '6':
                                    break
                    else:
                        print("No task found")
            case '6':
                print("Delete task")
            case '7':
                print("Search/Filter task")
            case '8':
                print("Exit")
                break
            case _:
                print("Option no valid")

if __name__ == '__main__':
    main()


