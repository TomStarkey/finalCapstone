# =====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"


# This class is used in the generate report function in order to store the data within objects.
class UserEntry:
    def __init__(self, username, assigned_tasks, percentage_of_total, percentage_complete) -> None:
        self.username = username
        self.assigned_tasks = assigned_tasks
        self.percentage_of_total = percentage_of_total
        self.percentage_complete = percentage_complete


# Only accepts input in format (YYYY-MM-DD)
def get_date():
    while True:
        try:
            date_string = input("Due date of task (YYYY-MM-DD): ")
            date_time_input = datetime.strptime(date_string, DATETIME_STRING_FORMAT)
            return date_time_input

        except ValueError:
            print("Invalid datetime format. Please use the format specified")


# Create tasks.txt if it doesn't exist and reads the content of the file.
def read_file(file_name):
    while True:
        if not os.path.exists(file_name):
            with open(file_name, "w"):
                pass
        else:
            with open(file_name, 'r') as task_file:
                task_data = task_file.read().split("\n")
                task_data = [t for t in task_data if t != ""]
                return task_data

            # Produce a tasklist


def produce_tlist(task_data):
    task_list = []
    task_number = 1
    for t_str in task_data:
        curr_t = {}

        # Split by semicolon and manually add each component
        task_components = t_str.split(";")
        curr_t['number'] = (task_components[0])
        curr_t['username'] = task_components[1]
        curr_t['title'] = task_components[2]
        curr_t['description'] = task_components[3]
        curr_t['due_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
        curr_t['assigned_date'] = datetime.strptime(task_components[5], DATETIME_STRING_FORMAT)
        curr_t['completed'] = True if task_components[6] == "Yes" else False

        task_number += 1
        task_list.append(curr_t)
    return task_list


# Extract user data from text file.
def define_userpass(file_name):
    # ====Login Section====
    """This code reads usernames and password from the user.txt file to
        allow a user to login.
    """
    # If no user.txt file, write one with a default account
    if not os.path.exists(file_name):
        with open(file_name, "w") as default_file:
            default_file.write("admin;password")

    # Read in user_data
    with open("user.txt", 'r') as user_file:
        user_info = user_file.read().split("\n")
        return user_info


# Assign text file data to username and password
def assign_userpass(user_info):
    login_info = {}
    for user in user_info:
        username, password = user.split(';')
        login_info[username] = password
    return login_info


# Request user login
def request_login(user_info):
    login_true = False
    while not login_true:

        print("LOGIN")
        current_user = input("Username: ")
        curr_pass = input("Password: ")
        if current_user not in user_info.keys():
            print("User does not exist")
            continue
        elif user_info[current_user] != curr_pass:
            print("Wrong password")
            continue
        else:
            print("Login Successful!")
            login_true = True
    return login_true, current_user


# Menu option - Register user
def reg_user(login_info):
    """Add a new user to the user.txt file"""
    # - Request input of a new username
    # Check user file for matching usernames.
    while True:
        new_username = input("New Username: ")
        duplicates = 0
        with open("user.txt", "r+") as user_file:
            users = user_file.readlines()
            for line in users:
                user = line.split(";")
                if user[0] == new_username:
                    duplicates += 1
                else:
                    continue

            if duplicates > 0:
                print("There is already a user by that name.")
            else:
                print("Your username has been created.")
                user_file.write("\n" + new_username + ";")
                break
    while True:
        # - Request input of a new password
        new_password = input("New Password: ")

        # - Request input of password confirmation.
        confirm_password = input("Confirm Password: ")

        # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            print("New user added")
            login_info[new_username] = new_password

            with open("user.txt", "w") as out_file:
                user_info = []
                for k in login_info:
                    user_info.append(f"{k};{login_info[k]}")
                out_file.write("\n".join(user_info))
                break

        # - Otherwise you present a relevant message.
        else:
            print("Passwords do no match")


# Menu option - Add task
def add_task():
    """Allow a user to add a new task to task.txt file
        Prompt a user for the following:
        - A username of the person whom the task is assigned to,
        - A title of a task,
        - A description of the task and
        - the due date of the task."""
    while True:
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
        else:
            break

    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    due_date_time = get_date()

    # Then get the current date.
    curr_date = date.today()
    new_task = {
        "number": str(total_tasks + 1),
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    tlist.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in tlist:
            str_attrs = [
                t['number'],
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")


# This function only accepts numerical values.
def get_number():
    while True:
        try:
            number = int(input("Please enter a number\n"))
            return number
        except ValueError:
            print("That is not a number")


# A feature for my task that requests whether the user would like to select a task then takes the input and checks
# for errors
def task_select(call_list):
    while True:
        print("Which task would you like to select? Enter -1 to return to the menu")
        task_number = get_number()
        if task_number == 0:
            print("There is no task by that number")
        elif task_number > 0:
            task_found = 0
            for task in call_list:
                if task["number"] == str(task_number):
                    task_found += 1
        elif task_number == -1:
            return task_number
        else:
            print("There is no task by that number")

        if task_found == 0:
            print("There is no task by that number")
            return False
        else:
            print(f"You have selected task{task_number}")
            return task_number


# Feature of view all that allows user to select a specific task based on number.
def call_task(task_number):
    task_selected = 0
    for t in tlist:
        print(task_selected)
        if task_number == t['number']:
            disp_str = f"Task number: \t {t['number']}\n"
            disp_str += f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)
            task_selected += 1
            print(f"Task {t['number']} has been selected")
            break
    while True:
        task_options = input("Would you like to A) edit the task or B) mark as complete")
        if task_options.upper() == "A":
            if t["completed"]:
                print("That task is already completed.")
                break
            else:
                edit_task(t)
            break
        elif task_options.upper() == "B":
            mark_as_complete(t)
            break
        else:
            print("Please select one of the given options.")

    while True:
        menu_option = input("Would you like to A) return to the menu or B) exit the program?")
        if menu_option.upper() == "A":
            return
        elif menu_option.upper() == "B":
            exit()
        else:
            print("Please select one of the given options")


# Changes "completed" key in task to True
def mark_as_complete(completed_task):
    update_tlist(completed_task, "completed", True)


# This function allows the user to search for tasks with particular criteria, e.g. any task with the same due date.
def find_by_element(element, value):
    items_found = 0
    relevant_tasks = []
    for t in tlist:
        if t[element] == value:
            items_found += 1
            relevant_tasks += [t]

    if items_found == 0:
        print(f"There is no task with the {element} as {value}")
    elif items_found > 0:
        print("These are the tasks relevant to your search:\n")

        for t in relevant_tasks:
            disp_str = f"Task number: \t {t['number']}\n"
            disp_str += f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)

        return relevant_tasks


# Takes a task, element and new value, adds this to the task data and then rewrites the file with the new data.
def update_tlist(task, element, new_value):
    for item in tlist:
        if item["number"] == task["number"]:
            while True:
                final_check = input(f"Are you sure that you would like to change the {element} to {new_value} (y/n)\n")
                if final_check.lower() == "y":
                    item[element] = new_value
                    break
                elif final_check.lower() == "n":
                    return
                else:
                    print("Please enter one of the options given.")

    with open(taskfile, "w") as updated_file:
        task_list_to_write = []
        for t in tlist:
            if t["number"] == task["number"]:
                str_attrs = [
                    task['number'],
                    task['username'],
                    task['title'],
                    task['description'],
                    task['due_date'].strftime(DATETIME_STRING_FORMAT),
                    task['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if task['completed'] else "No"
                ]
            else:
                str_attrs = [
                    t['number'],
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
            task_list_to_write.append(";".join(str_attrs))
        updated_file.write("\n".join(task_list_to_write))
    print("Task successfully updated.")


# When the user chooses to edit a task, the username of the person to whom the task is assigned or the due
# date of the task can be edited. The task can only be edited if it has not yet been completed.
def edit_task(task):
    # input what would you like to edit - taken as parameters.
    while True:
        edit_options = input("Would you like to edit A) The due date, or B) the assigned user")
        # due date
        if edit_options.upper() == "A":
            print(task["due_date"])
            print(f"The due date for the task currently is {task['due_date']}")
            while True:
                try:
                    task_due_date = input("Due date of task (YYYY-MM-DD): ")
                    new_due_date = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                    update_tlist(task, "due_date", new_due_date)
                    break

                except ValueError:
                    print("Invalid datetime format. Please use the format specified")

        # assigned person.
        elif edit_options.upper() == "B":
            while True:
                task_username = input("Name of new person assigned to task: ")
                if task_username not in username_password.keys():
                    print("User does not exist. Please enter a valid username")
                else:
                    break
            task["username"] = task_username
            new_assigned_user = task["username"]
            update_tlist(task, "username", new_assigned_user)
            break
        else:
            print("Please enter one of the given options.")


# Menu option - View all tasks
def view_all(task_list):
    """Reads the task from task.txt file and prints to the console in the
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling)
    """
    if not task_list:
        print("There are no tasks in the list")
        return
    else:
        call_list = []
        for t in task_list:
            disp_str = f"Task number: \t {t['number']}\n"
            disp_str += f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n{t['description']}\n"
            disp_str += f"Completed: \t" "Yes" if t['completed'] else "Completed: \t No"
            print(disp_str + "\n")

            call_list += [t]

    if curr_user == "admin":
        selected_number = task_select(call_list)
        if selected_number == -1:
            return
        else:
            call_task(str(selected_number))


# Menu option - View my tasks - This function needs updating.
def view_mine(task_list):
    """Reads the task from task.txt file and prints to the console in the
            format of Output 2 presented in the task pdf (i.e. includes spacing
            and labelling)
            """
    call_list = []
    for t in task_list:
        if t['username'] == curr_user:
            disp_str = f"\nTask number: \t {t['number']}\n"
            disp_str += f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n{t['description']}\n"
            disp_str += f"Completed: \t" "Yes" if t['completed'] else "Completed: \t No"
            print(disp_str + "\n")
            call_list += [t]

    if not call_list:
        print("You have no tasks assigned to you.")
        return False
    else:
        return call_list


def generate_report():
    overviewfile = "task_overview.txt"
    userfile = "user_overview.txt"
    if not os.path.exists(overviewfile):
        with open(overviewfile, "w"):
            pass
    if not os.path.exists(userfile):
        with open(overviewfile, "w"):
            pass

    if not tlist:
        with open(overviewfile, "a") as file:
            file.write("There are no tasks in the list.")
            return

    today = datetime.today()
    # Testing today var
    print(f"Today is: {today}")
    task_counter = 0
    total_completed_tasks = 0
    incomplete_tasks = 0
    overdue_task = 0
    for task in tlist:
        task_counter += 1
        if task["completed"]:
            total_completed_tasks += 1
        elif not task["completed"] and task['due_date'] < today:
            overdue_task += 1
        elif not task["completed"]:
            incomplete_tasks += 1

    percentage_incomplete = incomplete_tasks / task_counter * 100
    percentage_overdue = overdue_task / task_counter * 100

    overview_list = [f"Total tasks: {task_counter}",
                     f"Total complete tasks: {total_completed_tasks}",
                     f"Total incomplete tasks: {incomplete_tasks}",
                     f"Total overdue tasks: {overdue_task}",
                     f"Percentage tasks incomplete: {percentage_incomplete}",
                     f"Percentage tasks overdue: {percentage_overdue}"]

    # Write to task_overview.txt
    with open(overviewfile, "a") as overview:
        overview.write(f"Report generated on {today}\n" + "\n".join(overview_list))
        overview.write("\n\n")

    user_list = username_password.keys()
    total_users = len(user_list)
    user_info = []
    for user in user_list:
        assigned_tasks = 0
        completed_tasks = 0
        for task in tlist:
            if user == task["username"]:
                assigned_tasks += 1
            if user == task["username"] and task["completed"]:
                completed_tasks += 1
        if assigned_tasks == 0:

            percentage_of_total = 0
            percentage_complete = 0
        else:
            percentage_of_total = assigned_tasks / task_counter * 100
            percentage_complete = completed_tasks / assigned_tasks * 100

        user_entry = UserEntry(user, assigned_tasks, percentage_of_total, percentage_complete)
        user_info.append(user_entry)

    # WRITE THE USER DATA TO TEXTFILE "USER_OVERVIEW.TXT"
    with open(userfile, "a") as report:
        report.write(f"Report generated on {today}\n")
        for user in user_info:
            output = [f"Total users: {total_users}",
                      f"Total tasks: {task_counter}"
                      f"Username: {user.username}",
                      f"Assigned Tasks = {user.assigned_tasks}",
                      f"Percentage of Total tasks: {user.percentage_of_total}",
                      f"Percentage of users completed tasks: {user.percentage_complete}"]
            report.write("\n".join(output))
            report.write("\n\n")

    print("\nReports successfully generated.")


# Menu option - Display stats (admin only)
def display_stats(task_list):
    """If the user is an admin they can display statistics about number of users
                and tasks."""
    num_users = len(username_password.keys())
    num_tasks = len(task_list)

    print("-----------------------------------")
    print(f"Number of users: \t\t {num_users}")
    print(f"Number of tasks: \t\t {num_tasks}")
    print("-----------------------------------")


# Menu function displays choices and returns option choice.
def menu():
    if curr_user == "admin":
        print()
        menu_choice = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    gr - Generate report
    ds - Display statistics
    e - Exit
    ''').lower()
        return menu_choice
    else:
        print()
        menu_choice = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    ds - Display statistics
    e - Exit
    ''').lower()
        return menu_choice


# Initiating.
taskfile = "tasks.txt"
information = read_file(taskfile)
tlist = produce_tlist(information)
user_data = define_userpass("tasks.txt")
username_password = assign_userpass(user_data)
logged_in, curr_user = request_login(username_password)

# All the above functions fine. including the called functions.

# Main programme loop.
while True:
    # Update tlist
    information = read_file("tasks.txt")
    tlist = produce_tlist(information)
    total_tasks = len(tlist)
    if logged_in:
        # Initiating menu
        option_choice = menu()
        # Registering a user
        if option_choice == 'r':
            reg_user(username_password)
            # Adding a task
        elif option_choice == 'a':
            add_task()
        # View all tasks
        elif option_choice == 'va':
            view_all(tlist)
        # View MY tasks
        elif option_choice == 'vm':
            viewed_items = view_mine(tlist)
            if not viewed_items:
                pass
            else:
                selected_task_num = task_select(viewed_items)
                call_task(selected_task_num)
        # Generate report
        elif option_choice == "gr" and curr_user == "admin":
            generate_report()
        # Display statistics
        elif option_choice == 'ds' and curr_user == 'admin':
            display_stats(tlist)
        # Exit
        elif option_choice == 'e':
            print('Goodbye!!!')
            exit()
        else:
            print("Please enter a valid option.")
