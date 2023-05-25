from collections import deque

operators = {
    "a": lambda a, b: a + b,
    "s": lambda a, b: a - b,
    "d": lambda a, b: a / b if b != 0 else a,
    "m": lambda a, b: a * b,
}


def math_operations(*numbers, **operations):
    numbers = deque(numbers)

    while numbers:
        for key, value in operations.items():
            if not numbers:
                break

            number = numbers.popleft()
            operations[key] = operators[key](value, number)

    result = ""

    for key, value in sorted(operations.items(), key=lambda x: (-x[1], x[0])):
        result += f"{key}: {value:.1f}\n"

    return result


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))