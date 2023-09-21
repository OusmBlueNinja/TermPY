# ["reminder", "packages.reminder", ["reminder"]]
# Made By OusmBlueNinja
import time

# Dictionary to store reminders (task as key, timestamp as value)
reminders = {}

def reminder(command: list):
    if len(command) < 1:
        print("Usage: reminder [add/list/remove] [task] [optional: time (minutes)]")
        return

    action = command[0].lower()

    if action == "add":
        if len(command) < 2:
            print("Usage: reminder add [task] [optional: time (minutes)]")
            return

        task = command[1]
        timestamp = time.time()

        if len(command) > 2:
            try:
                minutes = float(command[2])
                timestamp += minutes * 60
            except ValueError:
                print("Invalid time format. Please specify the time in minutes.")
                return

        reminders[task] = timestamp
        print(f"Reminder added: {task}")

    elif action == "list":
        print("Current Reminders:")
        for task, timestamp in reminders.items():
            remaining_time = timestamp - time.time()
            print(f"{task} - {int(remaining_time / 60)} minutes remaining")

    elif action == "remove":
        if len(command) < 2:
            print("Usage: reminder remove [task]")
            return

        task = command[1]
        if task in reminders:
            del reminders[task]
            print(f"Reminder removed: {task}")
        else:
            print(f"No reminder found with the task: {task}")

    else:
        print("Invalid action. Use 'add', 'list', or 'remove'.")

