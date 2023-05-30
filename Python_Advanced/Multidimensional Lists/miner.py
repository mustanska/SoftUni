from collections import deque


def make_moves(moves, position):
    for row in range(n):
        if row != position[0]:
            continue
        for col in range(n):
            if col != position[1]:
                continue

            if moves:
                move = moves.popleft()
                move_row, move_col = directions[move]
                if check_index(row + move_row) and check_index(col + move_col):
                    return [row + move_row, col + move_col]
            else:
                return

    return position


def check_index(index):
    return 0 <= index < n


n = int(input())

commands = deque(input().split())

field = [input().split() for _ in range(n)]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
total_coals = sum([row.count("c") for row in field])
collected_coals = 0

miner_position = []

for i in range(n):
    for j in range(n):
        if field[i][j] == "s":
            miner_position.extend([i, j])

while True:
    result = make_moves(commands, miner_position)
    if not result:
        print(f"{total_coals - collected_coals} pieces of coal left. {(miner_position[0], miner_position[1])}")
        break

    miner_position = result
    current_row = miner_position[0]
    current_col = miner_position[1]

    if field[current_row][current_col] == "c":
        field[current_row][current_col] = "*"
        collected_coals += 1

        if collected_coals == total_coals:
            print(f"You collected all coal! {(miner_position[0], miner_position[1])}")
            break

    elif field[current_row][current_col] == "e":
        print(f"Game over! {(miner_position[0], miner_position[1])}")
        break
