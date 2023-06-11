SIZE = 6


def operation_perform(command_info):
    row = position[0] + directions[command_info[1]][0]
    col = position[1] + directions[command_info[1]][1]

    if command_info[0] == "Create":
        if matrix[row][col] == ".":
            matrix[row][col] = command_info[2]

    elif command_info[0] == "Update":
        if matrix[row][col].isalnum():
            matrix[row][col] = command_info[2]

    elif command_info[0] == "Delete":
        if matrix[row][col].isalnum():
            matrix[row][col] = "."

    elif command_info[0] == "Read":
        if matrix[row][col].isalnum():
            print(matrix[row][col])

    return [row, col]


matrix = [input().split() for _ in range(SIZE)]

position = [int(x) for x in input()[1:-1].split(", ")]

command = input()

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while command != "Stop":
    position = operation_perform(command.split(", "))

    command = input()

[print(*row, sep=" ") for row in matrix]