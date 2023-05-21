from collections import deque


def check_index(index, size):
    return 0 <= index < size


def player_move(position):
    for row in range(rows):
        if row != position[0]:
            continue
        for col in range(cols):
            if col != position[1]:
                continue

            command = commands.popleft()
            move_row, move_col = directions[command]
            move_row += row
            move_col += col

            if check_index(move_row, rows) and check_index(move_col, cols):
                position = [move_row, move_col]
            else:
                return

            return position


def find_bunnies_positions(field):
    positions = deque()
    for i in range(rows):
        for j in range(cols):
            if field[i][j] == "B":
                positions.append([i, j])

    return positions


def spread_of_bunnies(field):
    while bunnies_positions:
        bunny_row, bunny_col = bunnies_positions.popleft()

        for value in directions.values():
            direction_row = bunny_row + value[0]
            direction_col = bunny_col + value[1]

            if check_index(direction_row, rows) and check_index(direction_col, cols):
                field[direction_row][direction_col] = "B"

    return field


rows, cols = [int(x) for x in input().split()]

lair = [list(input()) for _ in range(rows)]

commands = deque(input())

directions = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
}

player_position = []

for i in range(rows):
    for j in range(cols):
        if lair[i][j] == "P":
            lair[i][j] = "."
            player_position.extend([i, j])

bunnies_positions = find_bunnies_positions(lair)

is_dead = False

while True:
    result = player_move(player_position)
    lair = spread_of_bunnies(lair)

    if not result:
        break

    player_position = result
    bunnies_positions = find_bunnies_positions(lair)

    if player_position in bunnies_positions:
        is_dead = True
        break

[print(*row, sep="") for row in lair]
if is_dead:
    print(f"dead: {' '.join(str(position) for position in player_position)}")
else:
    print(f"won: {' '.join(str(position) for position in player_position)}")