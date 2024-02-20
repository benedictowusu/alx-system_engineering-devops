import requests
import csv

def get_employee_todo_progress(employee_id):
    """Retrieves and displays the TODO list progress of a given employee using the REST API.
    Extends functionality to export data in CSV format.
    """

    # ... (rest of the code from the previous response)

    # Export data to CSV
    filename = f"{employee_id}.csv"
    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for task in todos:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": task["completed"],
                "TASK_TITLE": task["title"]
            })

    print(f"Data exported to CSV file: {filename}")
