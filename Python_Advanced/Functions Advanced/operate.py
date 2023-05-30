from functools import reduce


def operate(operator, *numbers):
    return reduce(operators[operator], numbers)


operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0,
}

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
