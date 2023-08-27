#["nano", "packages.nano", ["nano"]]

import os
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter

class TextEditor:
    def __init__(self):
        self.lines = []
        self.file = ""

    def load_file(self, filename):
        try:
            with open(filename, "r") as file:
                self.lines = file.readlines()
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

    def save_file(self, filename):
        if filename == "":
            filename = self.file
        with open(filename, "w") as file:
            file.writelines(self.lines)

    def edit(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.display()

            action = input("\nCommands: [e]dit, [n]ewline, [s]ave, [q]uit: ").lower()

            if action == "e":
                self.edit_lines()
            elif action == "n":
                self.newline()
            elif action == "s":
                filename = input("Enter filename to save: ")
                self.save_file(filename)
                print(f"File '{filename}' saved.")
            elif action == "q":
                print("Exiting the text editor.")
                break
            else:
                print("Invalid command.")

    def display(self):
        print("Editing: " + self.file)
        for i, line in enumerate(self.lines):
            highlighted_line = highlight(line, PythonLexer(), TerminalFormatter())
            print(f"{i + 1}: {highlighted_line}", end="")
            
    def newline(self):
        self.lines.append("\n")

    def edit_lines(self):
        line_number = int(input("Enter line number to edit: ")) - 1
        if 0 <= line_number < len(self.lines):
            new_line = input("Enter new text: ")
            self.lines[line_number] = new_line + "\n"
        else:
            print("Invalid line number.")


def nano(args):
    if len(args) != 1:
        print("Usage: nano <filename>")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        filename = args[0]
        
        editor = TextEditor()
        editor.file = filename
        editor.load_file(filename)
        editor.edit()