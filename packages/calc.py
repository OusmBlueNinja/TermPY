# ["calc", "packages.calc", ["calc"]]
# Made By YourNameHere

def calc(command: list):
    if len(command) != 3:
        print("Usage: calculator [operand1] [operator] [operand2]")
        return

    operand1 = float(command[0])
    operator = command[1]
    operand2 = float(command[2])

    result = None

    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        if operand2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = operand1 / operand2
    else:
        print("Invalid operator. Supported operators are +, -, *, /")
        return

    print(f"Result: {operand1} {operator} {operand2} = {result:.2f}")
