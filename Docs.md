# Docs

## Installing a package 

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
# made by OusmBlueNinja

def out(message):
    print(message)
```

From here you can run pretty much anything.