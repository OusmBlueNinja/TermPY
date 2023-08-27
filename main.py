import json
import os
import sys
import importlib
from inspect import isfunction
import random
import time
import ast
if os.name != "nt":
    import readline
import threading
import signal
import requests
import subprocess

helper = '''import ast
class color:
    green = "\033[1;32m"
    blue = "\033[1;34m"
    white = "\033[0m"
    green  = "\033[1;32m"
    red  = "\033[1;31m"
    white  = "\033[0m"
    blue  = "\033[1;34m"
    orange  = "\033[1;33m"

def update(self, packages):
        with open(("./packages/pakk.conf"), "w") as f:
                f.write(str(packages))
                
def toList(List: str) -> list:
        
        newList = ast.literal_eval(List)
        if isinstance(newList, list):
            return newList
                
def install(name:str, Packages:list):
    try:
            
            if name in [row[0] for row in Packages.packages]:
                return
            
            with open(("./packages/"+name+".py"), "r") as f:
                line = f.readline()
            
            line = line.strip("#")
           
            # ... (existing code)

            print("Installing Package")
            

            

            Packages.packages.append(toList(line))
            Packages.update(Packages.packages)
            print(f"{color.green}Success:{color.white} Successfully installed {name}.")

    except Exception as e:
        raise Exception(f"{color.red}{e}")'''


class color:
    green = "\033[1;32m"
    blue = "\033[1;34m"
    white = "\033[0m"
    red  = "\033[1;31m"
    orange  = "\033[1;33m"
    
def restart_program():
    python = sys.executable
    subprocess.call([python, __file__])
    sys.exit()

try:
    try:
        os.mkdir("./helper/")
        try:
            with open(f"./helper/helper.py", "w") as f:
                f.write(helper)
        except:
            print("err")
    except:
        pass
    os.mkdir("./packages/")
    with open(f"./packages/pakk.conf", "x") as f:
        f.close()
    
except:
    pass



    
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    

def call(full_module_name, func_name, *args, **kwargs):
    module = importlib.import_module(full_module_name)
    
    
    if func_name in dir(module):
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)
            if isfunction(attribute) and attribute_name == func_name:
                attribute(*args, **kwargs)
    else:
        raise Exception("Command Not Found")
            
            
def download(name: str, Packages: list):
                url = f"https://raw.githubusercontent.com/OusmBlueNinja/TermPY/main/packages/{name}.py"
                r = requests.get(url)
                #print(r.text)
                fileInstallingCreator = os.path.join(os.path.dirname(os.path.realpath(__file__)), "packages", name+".py")
                print("Saving file to disk")
                with open(fileInstallingCreator, "w") as newFile:
                    newFile.write(r.text)
                time.sleep(1)
                
                
            

def getPrompt():
    path = "USERNAME" if os.name == "nt" else "USER"
    username = os.environ.get(path)
    if username is None:
        username = ""
    path = os.getcwd()

    # Set up tab completion for file and directory names
    if os.name != "nt":
        completer = readline.get_completer()
        readline.set_completer_delims(' \t\n')
        readline.parse_and_bind("tab: complete")

    prompt = color.white + "┌ " + color.green + username + color.white + ":" + color.blue + path + color.white + "\n└ $ "
    return prompt




def getInput():
    print(getPrompt(), end="")
    return input()

def getIndex( packages:list, package: str) -> str:
    for key in packages:
        if packages[key] == package:
            return key



def toList(List: str) -> list:
        
        newList = ast.literal_eval(List)
        if isinstance(newList, list):
            return newList

class packages:
    def __init__(self):
        try:
            with open(("./packages/pakk.conf"), "r") as f:
                self.packages = toList(f.readline())
        except Exception as e:
            print(e)
            try:
                with open(("./packages/builtin.py"), "r") as f:
                    f.close()
                self.packages = [["builtin", "packages.builtin", ["echo", "ls", "rm", "clear", "cd", "ll"]]]
            except:
                self.packages = []
                download("builtin", self.packages)
                self.packages = [["builtin", "packages.builtin", ["echo", "ls", "rm", "clear", "cd", "ll"]]]
            self.update(self.packages)
    
        
        
    def update(self, packages):
        with open(("./packages/pakk.conf"), "w") as f:
                f.write(str(packages))


     
        
Packages = packages()       



class packagemanager:
    def __init__(self, args):
        
        if len(args) <= 1:
            print("Options:\ninstall <package name> | installs package \nlist                   | lists installed packages\nremove <package name>  | uninstall packages\navailable              | lists available commands")
       
        elif args[1] == "install":
            self.install(args[2])
        elif args[1] == "list":
            self.List()
        elif args[1] == "remove":
            self.uninstall(args[2:])
        elif args[1] == "available":
            self.commands("./packages")
        else:
            print("Options:\ninstall <package name> | installs package \nlist                   | lists installed packages\nremove <package name>  | uninstall packages\navailable              | lists available commands")
       
        return
    
    
    def commands(self, directory):
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.name.endswith(".py"):
                    package_name = entry.name[:-3]  # Remove the ".py" extension
                    if package_name not in [row[0] for row in Packages.packages]:
                        print(f"Package '{package_name}' is not installed.")
        
    
    def install(self, name: str) -> int:
        if name in [row[0] for row in Packages.packages]:
                raise Exception("Package already installed")
        try:
            if not os.path.exists(f"./packages/{name}.py"):
                raise FileNotFoundError(name)
                
            
        except FileNotFoundError:
                print("Downloading File from Source")
                download(name, Packages)
                call("helper.helper", "install", name, Packages)
                print(f"{color.orange}WARNING: {color.white}Restarting Program")
                restart_program() 
        except Exception as e:
            raise Exception(f"Package could not be found, make sure package source is in [ packages ] folder. {e}")
        
        try:
            
            if name in [row[0] for row in Packages.packages]:
                raise Exception("Package already installed")
            
            with open(("./packages/"+name+".py"), "r") as f:
                line = f.readline()
            
            line = line.strip("#")
           
            # ... (existing code)

            print("Installing Package")
            

            

            Packages.packages.append(toList(line))
            Packages.update(Packages.packages)
            print(f"\n{color.green}Success:{color.white} Successfully installed {name}.")

        except Exception as e:
            raise Exception(f"{color.red}{e}")



        
    def List(self):
        print("Installed Packages: \n"+ "\n".join([row[0] for row in Packages.packages]))
        
    def uninstall(self, package: list):
        for name in package:
            #print(Packages.packages)
            print(f"Uninstalling {name}")
            for package in Packages.packages:
                if name in package[0]:
                    Packages.packages.remove(package)
            Packages.update(Packages.packages)
            print(f"{color.green}Sucess:{color.white} Uninstalled {name}.")
                
        
        
        #print(Packages.packages)
        
        
        
    
    
 
        
    

def handleCommands(command: list) -> list: 
    
    try:
        if command[0] == "exit":
            quit()
        if command[0] == "help":
            print("Type pakk for more help installing packages" )
            return [0,None]
        if command[0] == "pakk":
            try:
                PackageManager = packagemanager(command)
            except Exception as e:
                print(e)
            
            
            return [0,None]

            
        
    except Exception as e:
        raise Exception(e)

    try:
        ran = False
        for package in Packages.packages:
            if command[0] in package[2]:
                call(package[1], command[0], command[1:])
                ran = True
                return [0,None]
        return [1, 'Command not Found']
    except Exception as e:
        print(e)
        return [1, "A Faital error has acured while running commmand"]



def main():
    while True:
        command = getInput()
        
        if command == "":
            pass
        else:
            command = command.split(" ")
            error = handleCommands(command)
            if error[0]==1:
                
                print(f"{color.red}ERROR{color.white}:{color.red} {error[1]}{color.white}")
                


def start():
    
    
        
    
    try:
        print("")
        main()
    except (KeyboardInterrupt, EOFError):
        restart_program()


if __name__ == '__main__':
    start()
