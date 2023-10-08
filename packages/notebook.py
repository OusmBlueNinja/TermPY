# ["notebook", "packages.notebook", ["create", "list", "read", "delete"]]
# Made By OusmBlueNinja

# Dictionary to store notes (note name as key, note content as value)
notes = {}

def create(command: list):
    if len(command) != 2:
        print("Usage: create [note_name] [note_content]")
        return

    note_name = command[0]
    note_content = command[1]
    notes[note_name] = note_content
    print(f"Note '{note_name}' created successfully.")

def list_notes(command: list):
    if len(command) != 0:
        print("Usage: list")
        return

    if notes:
        print("Available notes:")
        for note_name in notes:
            print(note_name)
    else:
        print("No notes available.")

def read(command: list):
    if len(command) != 1:
        print("Usage: read [note_name]")
        return

    note_name = command[0]
    if note_name in notes:
        print(f"Note '{note_name}':\n{notes[note_name]}")
    else:
        print(f"Note '{note_name}' not found.")

def delete(command: list):
    if len(command) != 1:
        print("Usage: delete [note_name]")
        return

    note_name = command[0]
    if note_name in notes:
        del notes[note_name]
        print(f"Note '{note_name}' deleted successfully.")
    else:
        print(f"Note '{note_name}' not found.")

# Example usage:
# notebook ["create", "my_note", "This is my note content."]
# notebook ["list"]
# notebook ["read", "my_note"]
# notebook ["delete", "my_note"]
