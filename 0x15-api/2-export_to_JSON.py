#!/usr/bin/python3
import requests
import json

def get_employee_todo_progress(employee_id):
    """Retrieves and displays TODO list progress of an employee, optionally exporting data as JSON."""

    # Validate employee ID
    if not isinstance(employee_id, int) or employee_id <= 0:
        raise ValueError("Employee ID should be a positive integer.")

    # Construct API endpoint URLs
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    try:
        # Send GET requests
        todo_response = requests.get(todo_url)
        user_response = requests.get(user_url)

        todo_response.raise_for_status()
        user_response.raise_for_status()

        # Parse JSON responses
        todos = todo_response.json()
        user = user_response.json()

        # Extract employee name
        employee_name = user["name"]

        # Count completed and total tasks
        number_of_done_tasks = len([todo for todo in todos if todo["completed"]])
        total_number_of_tasks = len(todos)

        # Display progress summary (optional)
        print(f"Employee {employee_name} is done with tasks ({number_of_done_tasks}/{total_number_of_tasks}):")
        for task in todos:
            if task["completed"]:
                print("\t", task["title"])

        # Prepare data for JSON export
        tasks_data = []
        for task in todos:
            tasks_data.append({
                "task": task["title"],
                "completed": task["completed"],
                "username": user["username"],
            })

        # Export data to JSON file
        with open(f"{employee_id}.json", "w") as outfile:
            json.dump({
                "USER_ID": tasks_data
            }, outfile, indent=4)

        print(f"Employee data exported to {employee_id}.json")

    except requests.exceptions.RequestException as error:
        print(f"Error fetching data from API: {error}")

if __name__ == "__main__":
    employee_id = int(input("Enter employee ID: "))
    get_employee_todo_progress(employee_id)
