import curses

def main(stdscr):
    curses.curs_set(1)  # Show cursor
    stdscr.addstr(0, 0, "Simple Text Editor - Press Ctrl-G to exit")
    stdscr.refresh()
    
    text = []
    row, col = 1, 0
    
    while True:
        stdscr.move(row, col)
        key = stdscr.getch()

        if key == 7:  # Ctrl-G to exit
            break
        elif key == 10:  # Enter key
            text.append("")
            row += 1
            col = 0
        elif key == curses.KEY_BACKSPACE or key == 127:  # Backspace key
            if col > 0:
                col -= 1
                stdscr.delch(row, col)
                text[row - 1] = text[row - 1][:col] + text[row - 1][col + 1:]
        elif key == curses.KEY_LEFT:
            col = max(col - 1, 0)
        elif key == curses.KEY_RIGHT:
            col = min(col + 1, len(text[row - 1]))
        else:
            char = chr(key)
            stdscr.addch(row, col, char)
            if col == len(text[row - 1]):
                text[row - 1] += char
            else:
                text[row - 1] = text[row - 1][:col] + char + text[row - 1][col:]
            col += 1

        stdscr.refresh()

def tedit(args):
    curses.wrapper(main)
