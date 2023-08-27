#["netget", "packages.netget", ["netget"]]
# Made By OusmeBlueNinja
import os, sys


def netget(command: list):
    
    #print(command, len(command))
    if len(command) != 2:
        print("comand requires [ url ] [ path ]")
    
    url = command[0]
    location = command[1]
    try:
        import wget
        wget.download(url, location)
    except ImportError:
        os.system(f"wget {url} -O {location}")
        
    except:
        print("cannot download")
        

