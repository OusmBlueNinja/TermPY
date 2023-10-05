# ["filemanip", "packages.filemanip", ["mv", "cp"]]
import os
import shutil
 
def mv(command: list):
    if len(command) != 2:
        print("Usage: mv [source] [destination]")
        return
 
    source = command[0]
    destination = command[1]
 
    try:
        shutil.move(source, destination)
        print(f"Moved '{source}' to '{destination}'")
    except Exception as e:
        print(f"Error moving '{source}' to '{destination}': {str(e)}")
 
def cp(command: list):
    if len(command) != 2:
        print("Usage: cp [source] [destination]")
        return
 
    source = command[0]
    destination = command[1]
 
    try:
        shutil.copy2(source, destination)
        print(f"Copied '{source}' to '{destination}'")
    except Exception as e:
        print(f"Error copying '{source}' to '{destination}': {str(e)}")
 
# made by OusmBlueNinja

