SIZE = 6


def operation_perform(operation, direction, value=""):
    row = position[0] + directions[direction][0]
    col = position[1] + directions[direction][1]

    if operation == "Create":
        if matrix[row][col] == ".":
            matrix[row][col] = value

    elif operation == "Update":
        if matrix[row][col].isalnum():
            matrix[row][col] = value

    elif operation == "Delete":
        if matrix[row][col].isalnum():
            matrix[row][col] = "."

    elif operation == "Read":
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
    position = operation_perform(*command.split(", "))

    command = input()

[print(*row, sep=" ") for row in matrix]