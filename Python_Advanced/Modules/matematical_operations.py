first_number, sign, second_number = [float(x) if x.replace(".", "").isdigit() else x for x in input().split()]

operations = {
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "^": lambda a, b: a ** b,
}

try:
    result = round(operations[sign](first_number, second_number), 2)
except ZeroDivisionError:
    result = "Can't divide by zero"

print(result)