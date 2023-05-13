from collections import deque

number_of_commands = int(input())
stack = deque()

map_functions = {
    "1": lambda x: stack.append(x[1]),
    "2": lambda x: stack.pop() if stack else None,
    "3": lambda x: print(max(stack)) if stack else None,
    "4": lambda x: print(min(stack)) if stack else None
}

for _ in range(number_of_commands):
    command_data = input().split()

    map_functions[command_data[0]](command_data)

stack.reverse()
print(*stack, sep=", ")
