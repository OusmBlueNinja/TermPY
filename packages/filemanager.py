# ["filemanager", "packages.filemanager", ["filemanager"]]
# Made By OusmBlueNinja
import os

def filemanager(command: list):
    if len(command) > 1:
        print("Usage: filemanager [optional: directory_path]")
        return

    if len(command) == 1:
        directory_path = command[0]
    else:
        directory_path = os.getcwd()  # Use the current working directory as the default

    while True:
        print("\nOptions:")
        print("1. List Files")
        print("2. Create File")
        print("3. Delete File")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            list_files(directory_path)
        elif choice == "2":
            create_file(directory_path)
        elif choice == "3":
            delete_file(directory_path)
        elif choice == "4":
            print("Exiting File Manager.")
            break
        else:
            print("Invalid option. Please select a valid option (1, 2, 3, or 4).")

def list_files(directory_path):
    try:
        files = os.listdir(directory_path)
        if not files:
            print("The directory is empty.")
        else:
            print("Files in the directory:")
            for file in files:
                print(file)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def create_file(directory_path):
    try:
        file_name = input("Enter the name of the file to create: ")
        file_path = os.path.join(directory_path, file_name)

        if not os.path.exists(file_path):
            with open(file_path, "w"):
                pass  # Create an empty file
            print(f"File '{file_name}' created successfully.")
        else:
            print(f"File '{file_name}' already exists in the directory.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def delete_file(directory_path):
    try:
        file_name = input("Enter the name of the file to delete: ")
        file_path = os.path.join(directory_path, file_name)

        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File '{file_name}' deleted successfully.")
        else:
            print(f"File '{file_name}' does not exist in the directory.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
