from database_schema import create_database
from projects import add_project, show_projects
from validation import fast_travel, valid_number, existing_project, existing_task
import datetime
import tasks

def main():
    
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
                            break
                        case _:
                            print("Select a valid option")
            case '5':
                    print("Update task menu.")
                    project_id = valid_number("project id")
                    if existing_project(project_id):
                        task_id = valid_number("task id")
                        if existing_task(project_id, task_id):
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
                                        tasks.update_name(project_id, task_id)
                                        if not fast_travel("updating tasks"):
                                            break                  
                                    case '2':
                                        print("Update description") 
                                        tasks.update_description(project_id, task_id)
                                        if not fast_travel("updating tasks"):
                                            break  
                                    case '3':
                                        print("Update due date") 
                                        tasks.update_due_date(project_id, task_id)
                                        if not fast_travel("updating tasks"):
                                            break 
                                    case '4':
                                        print("Update status")
                                        tasks.update_status(project_id, task_id)
                                        if not fast_travel("updating tasks"):
                                            break   
                                    case '5':
                                        print("Update priority")
                                        tasks.update_priority(project_id, task_id)
                                        if not fast_travel("updating tasks"):
                                            break 
                                    case '6':
                                        break
                        else:
                            print("No task found")
                    else:
                        print("No project was found")
            case '6':
                print("Delete task")                
                tries = 0
                while True and tries < 3:
                    project_id = valid_number("project id")
                    if existing_project(project_id):
                        task_id = valid_number("task id")
                        if existing_task(project_id, task_id):
                            tasks.delete_task(project_id,task_id)
                            break
                        else:
                            tries += 1
                            print(f"No task was found {3 - tries} tries left.")
                    else:
                        tries += 1
                        print(f"No project was found {3 - tries} tries left.")
            case '7':
                print("Filter tasks")
                while True:
                    filter_tasks_by = input(f"""
                        {'*' * 30}
                        1. Priority 
                        2. Completed
                        3. Pending
                        4. Due date passed
                        5. On time
                        6. Back
                        {'*' * 30}
                        Option: """).strip()
                    match filter_tasks_by:
                        case '1':
                            task_priorities = { 1:"Low", 2:"Medium", 3:"High" }
                            priority = valid_number(""" a valid priority
                                1. Low
                                2. Medium
                                3. High
                            """)
                            if priority in task_priorities:
                                tasks.filter_by_priority(task_priorities[priority])
                                if not fast_travel("filtering tasks"):
                                    break              
                            else:
                                print("Choose a valid priority")                  
                        case '2':
                            print("Filter by completed") 
                            tasks.filter_by_status(True)
                            if not fast_travel("filtering tasks"):
                                break  
                        case '3':
                            print("Filter by pending...") 
                            tasks.filter_by_status(False)
                            if not fast_travel("filtering tasks"):
                                break 
                        case '4':
                            print("Filter by due time passed")
                            tasks.filter_by_date(datetime.date.today(), False)
                            if not fast_travel("filtering tasks"):
                                break   
                        case '5':
                            print("Filber by on time")
                            tasks.filter_by_date(datetime.date.today(), True)
                            if not fast_travel("filtering tasks"):
                                break 
                        case '6':
                            break
            case '8':
                print("Exit")
                break
            case _:
                print("Option no valid")

if __name__ == '__main__':
    main()


