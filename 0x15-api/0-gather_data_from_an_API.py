#!/usr/bin/python3
import requests

def get_employee_todo_progress(employee_id):
    """Retrieves and displays the TODO list progress of a given employee using the REST API."""

    # Validate employee ID
    if not isinstance(employee_id, int) or employee_id <= 0:
        raise ValueError("Employee ID should be a positive integer.")

    # Construct API endpoint URL
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    try:
        # Send GET request to API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        # Parse JSON response
        todos = response.json()

        # Extract employee name
        employee_name = next(user for user in requests.get("https://jsonplaceholder.typicode.com/users").json()
                             if user["id"] == employee_id)["name"]

        # Count completed and total tasks
        number_of_done_tasks = len([todo for todo in todos if todo["completed"]])
        total_number_of_tasks = len(todos)

        # Display progress summary
        print(f"Employee {employee_name} is done with tasks ({number_of_done_tasks}/{total_number_of_tasks}):")

        # Display completed tasks with proper formatting
        for task in todos:
            if task["completed"]:
                print("\t", task["title"])

    except requests.exceptions.RequestException as error:
        print(f"Error fetching data from API: {error}")

if __name__ == "__main__":
    employee_id = int(input("Enter employee ID: "))
    get_employee_todo_progress(employee_id)
