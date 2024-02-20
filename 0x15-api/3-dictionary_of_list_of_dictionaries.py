import requests
import json

def get_all_employee_todo_data():
    """Retrieves and combines TODO data for all employees into a JSON dictionary."""

    all_data = {}
    try:
        # Get response for all users
        user_response = requests.get("https://jsonplaceholder.typicode.com/users").json()

        # Get tasks for each user
        for user in user_response:
            user_id = user["id"]
            user_name = user["name"]
            url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
            task_response = requests.get(url).json()

            user_tasks = []
            for task in task_response:
                user_tasks.append({
                    "username": user_name,
                    "task": task["title"],
                    "completed": task["completed"]
                })

            all_data[user_id] = user_tasks

        # Write data to JSON file
        with open("todo_all_employees.json", "w") as outfile:
            json.dump(all_data, outfile, indent=4)

        print("Successfully exported all employee TODO data to todo_all_employees.json")

    except requests.exceptions.RequestException as error:
        print(f"Error fetching data from API: {error}")

if __name__ == "__main__":
    get_all_employee_todo_data()
