n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    line = input()

    if line == "END":
        [print(*row) for row in matrix]
        break

    command, *command_data = line.split()
    row, col, number = [int(x) for x in command_data]

    if 0 <= int(row) < n and 0 <= int(col) < n:
        if command == "Add":
            matrix[row][col] += number
        elif command == "Subtract":
            matrix[row][col] -= number
    else:
        print("Invalid coordinates")
