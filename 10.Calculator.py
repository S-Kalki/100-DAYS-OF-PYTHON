print("""
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
""")

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

power = "on"

while power == "on":

    n1 = float(input("What is the first number? "))

    while True:

        operation = input("Choose (+, -, *, /): ")

        n2 = float(input("What is the second number? "))

        answer = operations[operation](n1, n2)

        print(f"{n1} {operation} {n2} = {answer}")

        choice = input(
            "Type 'SAME' to continue with the answer,\n"
            "'START' to begin a new calculation,\n"
            "'OFF' to exit: "
        ).upper()

        if choice == "SAME":
            n1 = answer

        elif choice == "START":
            break

        elif choice == "OFF":
            power = "off"
            break