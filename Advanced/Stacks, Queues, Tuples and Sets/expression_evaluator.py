from collections import deque

expression = deque(input().split())

idx = 0

operations = {
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
}

while len(expression) > 1:
    element = expression[idx]

    if element in operations.keys():
        for _ in range(idx - 1):
            expression.appendleft(operations[element](int(expression.popleft()), int(expression.popleft())))
            idx = 0

        del expression[1]

    idx += 1

print(*expression)