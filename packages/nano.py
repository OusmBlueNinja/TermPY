#["nano", "packages.nano", ["nano"]]

import os, time
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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

            action = input("\nCommands: [e]dit, [b]ulk-edit, [n]ewline, [s]ave, [q]uit: ").lower()

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

            elif action == 'b':
                try:
                    
                    self.b_edit_lines()
                    filename = self.file
                    self.save_file(filename)
                    print(f"File '{filename}' saved.")
                except KeyboardInterrupt:
                    self.save_file(filename)
                    print(f"File '{filename}' saved.")
                    
                
            else:
                print("Invalid command.")

    def display(self):
        print("Editing: " + self.file)
        termSize = os.get_terminal_size()
        colms = termSize[0]
        for i, line in enumerate(self.lines):
            highlighted_line = highlight(line, PythonLexer(), TerminalFormatter())
            print(f"{i + 1}: {highlighted_line}", end="")
            
    def newline(self):
        self.lines.append("\n")

    def edit_lines(self):
        line_number = int(input("Enter line number to edit: ")) - 1
        while line_number >= len(self.lines):
            self.newline()
        if 0 <= line_number < len(self.lines):
            new_line = input("Enter new text: ")
            self.lines[line_number] = new_line + "\n"
        else:
            print("Invalid line number.")
            
    def b_edit_lines(self):
        
        line_number = int(input("Enter line number to start: ")) - 1
        #print(line_number, len(self.lines))
        
        if line_number <= -1:
            print("Invalid line number.")
            return
        
        while line_number >= len(self.lines):
            self.newline()
        #if -1 < line_number < len(self.lines):
            #print("Invalid line number.")
            #return
        clear()
        self.display()
        
        while True:
            clear()
            self.display()
            if line_number >= len(self.lines):
                self.newline()
            
            print(f"\n{' '*(len(str(line_number))+1)} {highlight(self.lines[line_number], PythonLexer(), TerminalFormatter())}", end="")
            new_line = input(f"{line_number+1}: ")
            if new_line == "":
                new_line = " "
            if new_line[0] == ':':
                command = new_line.split(" ")
                if command[0] == ":h":
                    print("Commands:\n  :q -> save and return to prompt\n  :g -> goto line number <:g 11> (goes to line 11)")
                    time.sleep(5)
                    clear()
                    continue
                elif command[0] == ":q":
                    self.save_file("")
                    break
                elif command[0] == ":g":
                    gotoLine = int(command[1])   
                    
                    line_number = gotoLine -1
                    continue
                
                
                
            self.lines[line_number] = new_line + "\n"
            line_number +=1

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
