#["pip", "packages.pip", ["pip"]]
# Made By Blurple
import os, sys


def pip(command: list):
    
    print(command, len(command))
    if len(command) != 1:
        print("comand requires [ package_name ] [ args (optional) ] ")
        return
    
    package = command[0]
    try:
        from pip._internal import main as pipmain
        pipmain(['install', {package}])
    except ImportError:
        os.system(f"pip install {package}")
    
    except:
        print("cannot download")
        
# im trying to make a pip command so i can install from in the app