import ast
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
            print(f"\n{color.green}Success:{color.white} Successfully installed {name}.")

    except Exception as e:
        raise Exception(f"{color.red}{e}")
