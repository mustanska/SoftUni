size = int(input())

field = [[int(x) if x.lstrip("-").isdigit() else x for x in input().split()] for _ in range(size)]

bunny_position = []

for i in range(size):
    for j in range(size):
        if field[i][j] == "B":
            bunny_position.extend([i, j])

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

max_sum_eggs = 0
max_sum_path = []
direction = ""

for move, move_coordinates in moves.items():
    move_row = bunny_position[0] + move_coordinates[0]
    move_col = bunny_position[1] + move_coordinates[1]

    sum_eggs = 0
    path = []

    while 0 <= move_row < size and 0 <= move_col < size:
        element = field[move_row][move_col]
        if element == "X":
            break

        sum_eggs += element
        path.append([move_row, move_col])
        move_row += move_coordinates[0]
        move_col += move_coordinates[1]

    if sum_eggs >= max_sum_eggs:
        max_sum_eggs = sum_eggs
        max_sum_path = path
        direction = move

print(direction)
print(*max_sum_path, sep="\n")
print(max_sum_eggs)
