from functools import reduce

expression = input().split()

functions = {
    "*": lambda i: reduce(lambda a, b: a * b, map(int, expression[:i])),
    "/": lambda i: reduce(lambda a, b: a // b, map(int, expression[:i])),
    "+": lambda i: reduce(lambda a, b: a + b, map(int, expression[:i])),
    "-": lambda i: reduce(lambda a, b: a - b, map(int, expression[:i])),

}

idx = 0

while len(expression) > 1:
    element = expression[idx]

    if element in functions.keys():
        expression[0] = functions[element](idx)
        [expression.pop(1) for i in range(idx)]
        idx = 0

    idx += 1

print(*expression)