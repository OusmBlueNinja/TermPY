import os
import curses
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter

class TextEditor:
    def __init__(self):
        self.lines = []
        self.file = ""
        self.cursor = (0, 0)  # (line, column)

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

    def edit(self, stdscr):
        self.stdscr = stdscr
        curses.curs_set(1)  # Show cursor
        self.stdscr.clear()
        self.display()

        while True:
            key = self.stdscr.getch()

            if key == curses.KEY_UP:
                self.move_cursor(-1)
            elif key == curses.KEY_DOWN:
                self.move_cursor(1)
            elif key == curses.KEY_LEFT:
                self.move_cursor(0, -1)
            elif key == curses.KEY_RIGHT:
                self.move_cursor(0, 1)
            elif key == ord('\n'):
                self.newline()
            elif key == curses.KEY_BACKSPACE or key == 127:
                self.delete_character()
            elif key == 19:  # Ctrl + S
                filename = input("Enter filename to save: ")
                self.save_file(filename)
                print(f"File '{filename}' saved.")
            elif key == 17:  # Ctrl + Q
                print("Exiting the text editor.")
                break
            elif key >= 32 and key <= 126:
                self.insert_character(chr(key))
            elif key == 27:  # Escape key
                pass

            self.stdscr.clear()
            self.display()

    def display(self):
        self.stdscr.addstr(0, 0, "Editing: " + self.file)
        for i, line in enumerate(self.lines):
            highlighted_line = highlight(line, PythonLexer(), TerminalFormatter())
            if i == self.cursor[0]:
                cursor_column = self.cursor[1]
                self.stdscr.addstr(i + 1, 0, f"{i + 1}: {highlighted_line[:cursor_column]}{highlighted_line[cursor_column:]}")
            else:
                self.stdscr.addstr(i + 1, 0, f"{i + 1}: {highlighted_line}")

    def move_cursor(self, line_change=0, column_change=0):
        new_line = self.cursor[0] + line_change
        new_column = self.cursor[1] + column_change

        if 0 <= new_line < len(self.lines):
            line_length = len(self.lines[new_line])
            new_column = max(0, min(new_column, line_length))
            self.cursor = (new_line, new_column)

    def newline(self):
        line, column = self.cursor
        self.lines[line] = self.lines[line][:column] + '\n' + self.lines[line][column:]
        self.move_cursor(1, 0)

    def delete_character(self):
        line, column = self.cursor
        if column > 0:
            self.lines[line] = self.lines[line][:column - 1] + self.lines[line][column:]
            self.move_cursor(0, -1)
        elif line > 0:
            prev_line_len = len(self.lines[line - 1])
            self.lines[line - 1] = self.lines[line - 1][:-1] + self.lines[line]
            self.lines.pop(line)
            self.move_cursor(-1, prev_line_len)

    def insert_character(self, char):
        line, column = self.cursor
        self.lines[line] = self.lines[line][:column] + char + self.lines[line][column:]
        self.move_cursor(0, 1)


def nano(args):
    if len(args) != 1:
        print("Usage: nano <filename>")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        filename = args[0]

        editor = TextEditor()
        editor.file = filename
        editor.load_file(filename)
        curses.wrapper(editor.edit)