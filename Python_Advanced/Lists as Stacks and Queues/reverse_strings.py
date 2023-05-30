string = input()

stack = list(string)

while stack:
    print(stack.pop(), end="")