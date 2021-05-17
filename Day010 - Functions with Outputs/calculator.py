import os

clear = lambda: os.system("clear")
clear()


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
    "/": divide,
}

num1 = float(input("what is the first number?: "))

answer = num1
anotherOperation = True

while anotherOperation:
    for key in operations:
        print(key)

    operation = input("Pick an operation to enact from the 4 lines above: ")
    num2 = float(input("what is the second number?: "))

    num1 = answer
    answer = operations[operation](answer, num2)

    print(f"{num1} {operation} {num2} = {answer}")

    anotherOp = input(
        "Enter y to perform another operation on this answer or n to stop: "
    )

    if anotherOp == "n":
        anotherOperation = False
