#["pip", "packages.pip", ["pip"]]
# Made By Blurple
import os, sys

def pip(command: list):
    
    #print(command, len(command))
    if len(command) != 1:
        print("comand requires [ package_name ] [ args (optional) ] ")
        return
    
    package = command[0]
    try:
        print("Running pip from shell")
        os.system(f"python -m pip install {package}")
    except Exception as e:
        print(e)
        
    
    except:
        print("cannot download")