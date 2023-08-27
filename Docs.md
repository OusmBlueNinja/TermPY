# Docs

## Installing a package 

1. download package source 
2. copy `(package).py` file to `./packages/`
3. restart `main.py`
4. run the command `pakk install <package name>`
5. run any command in the package

### the `pakk install` command will pull from internet in a future update
## Creating a package

Once the package is installed, you can use the commands in it, here is how to make one.

The top of the file must look like this;

```python
#["name", "package.<package name>", ["commands, command"]]
# made by <your name here>
```

then, to write a command, just write a function with the code you want to run, take this for example;

```python
#["echo", "package.echo", ["out"]]
# made by <Your name Here>

#Function name and command must be the same
def out(message):
    print(message)
```

From here you can run pretty much anything.


```python 
#["test", "package.test", ["hello"]]
#you can even do classes

class test:
    def __init__(self):
        self.hello = "World"

    def func(self):
        print(self.hello)

def hello(args):
    del args
    test = test()
    test.func()

```


