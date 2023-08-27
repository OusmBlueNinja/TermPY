#["builtin", "packages.builtin", ["echo", "ls", "rm", "clear", "cd", "ll"]]
import os
import stat

if os.name != 'nt':
    import pwd
    import grp
import time




def echo(message: list) -> int:
    try:
        print(" ".join(message))
    except:
        return
    
def ls(args):
    del args
    
    
    pass

def rm(files: list):
    for file in files:
        os.remove(file)
        
def clear(args):
    del args
    os.system('cls' if os.name == 'nt' else 'clear')
    


def cd(args):
    if len(args) == 0 or args[0] == "~":
        new_path = os.path.expanduser("~")  # Get the home directory path
    elif len(args) == 1:
        new_path = os.path.abspath(args[0])  # Get the absolute path
    else:
        print("Usage: cd <path> or cd ~")
        return

    try:
        os.chdir(new_path)  # Change the current working directory
    except FileNotFoundError:
        print("Directory not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



def ls(args):
    del args  # You can remove this line if you're not using args

    blue_color = '\033[34m'
    green_color = '\033[32m'
    white_color = '\033[37m'
    reset_color = '\033[0m'

    dir_path = os.getcwd()
    try:
        with os.scandir(dir_path) as entries:
            for entry in entries:
                if not entry.name.startswith('.'):
                    file_path = os.path.join(dir_path, entry.name)
                    file_stat = os.stat(file_path)
                    if stat.S_ISDIR(file_stat.st_mode):
                        print(blue_color + entry.name + '/' + reset_color, end=' ')
                    elif file_stat.st_mode & stat.S_IXUSR:
                        print(green_color + entry.name + '*' + reset_color, end=' ')
                    else:
                        print(white_color + entry.name + reset_color, end=' ')
            print()  # Newline after listing
    except Exception as e:
        print(f"An error occurred: {e}")
        
        
def ll(args):
    if os.name != 'nt':
        print("This command only works for linux")
        return
    dir_path = os.getcwd()

    green_color = '\033[32m'
    blue_color = '\033[34m'
    whiteColor = '\033[37m'
    orange_color = '\033[33m'
    reset_color = '\033[0m'

    try:
        with os.scandir(dir_path) as entries:
            for entry in entries:
                file_stat = entry.stat()
                file_name = entry.name
                
                if os.name != 'nt':
                    pw = pwd.getpwuid(file_stat.st_uid)
                    gr = grp.getgrgid(file_stat.st_gid)

                is_hidden = (file_name and file_name[0] == '.')

                time_str = time.ctime(file_stat.st_mtime)
                if time_str.endswith('\n'):
                    time_str = time_str[:-1]  # Remove newline character

                permission_str = (
                    (green_color + "r" if file_stat.st_mode & stat.S_IRUSR else whiteColor + "-") +
                    (blue_color + "w" if file_stat.st_mode & stat.S_IWUSR else whiteColor + "-") +
                    ((orange_color if is_hidden else green_color) + "x" if file_stat.st_mode & stat.S_IXUSR else whiteColor + "-") +
                    (green_color + "r" if file_stat.st_mode & stat.S_IRGRP else whiteColor + "-") +
                    (blue_color + "w" if file_stat.st_mode & stat.S_IWGRP else whiteColor + "-") +
                    ((orange_color if is_hidden else green_color) + "x" if file_stat.st_mode & stat.S_IXGRP else whiteColor + "-") +
                    (green_color + "r" if file_stat.st_mode & stat.S_IROTH else whiteColor + "-") +
                    (blue_color + "w" if file_stat.st_mode & stat.S_IWOTH else whiteColor + "-") +
                    ((orange_color if is_hidden else green_color) + "x" if file_stat.st_mode & stat.S_IXOTH else whiteColor + "-")
                )

                print(
                    "{:<11}{:>4} {:<8} {:<8} {:>8} {} {}{}".format(
                        permission_str,
                        file_stat.st_nlink,
                        pw.pw_name,
                        gr.gr_name,
                        file_stat.st_size,
                        time_str,
                        (blue_color if entry.is_dir() else (orange_color if is_hidden else green_color) if file_stat.st_mode & stat.S_IXUSR else whiteColor),
                        file_name,
                        reset_color
                    )
                )
    except Exception as e:
        print(f"An error occurred: {e}")
