size = int(input())

bombs_position = []

for _ in range(int(input())):
    line = input()[1:-1]

    position = [int(x) for x in line.split(", ")]
    bombs_position.append(position)

field = [[0] * size for _ in range(size)]

directions = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (1, 1),
    (-1, 1),
    (1, -1),
)

for bomb_row, bomb_col in bombs_position:
    field[bomb_row][bomb_col] = "*"

for current_row in range(size):
    for current_col in range(size):
        if field[current_row][current_col] == "*":
            for direction_row, direction_col in directions:
                row = direction_row + current_row
                col = direction_col + current_col

                if not(0 <= row < size and 0 <= col < size) or [row, col] in bombs_position:
                    continue

                field[row][col] += 1

[print(" ".join([str(el) for el in row])) for row in field]