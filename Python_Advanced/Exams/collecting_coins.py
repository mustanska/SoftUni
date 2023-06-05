def find_correct_index(index):
    if index < 0:
        return size - 1

    elif index >= size:
        return 0

    return index


def player_move(player_row, player_col):
    player_row = find_correct_index(player_row)
    player_col = find_correct_index(player_col)

    coins = field[player_row][player_col]
    field[player_row][player_col] = 0

    return [player_row, player_col], coins


size = int(input())

field = []
player_position = []

for row in range(size):
    field.append([int(el) if el.isdigit() else el for el in input().split()])

    if "P" in field[row]:
        player_position.extend([row, field[row].index("P")])
        field[row][field[row].index("P")] = 0

total_coins = 0
player_path = [player_position]

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while total_coins < 100:
    command = input()

    if command not in moves.keys():
        continue

    move_row = moves[command][0] + player_position[0]
    move_col = moves[command][1] + player_position[1]

    result = player_move(move_row, move_col)

    player_position = result[0]
    player_path.append(player_position)

    if result[1] == "X":
        total_coins //= 2
        print(f"Game over! You've collected {total_coins} coins.")
        break

    total_coins += result[1]

else:
    print(f"You won! You've collected {total_coins} coins.")

print("Your path:")
print(*player_path, sep="\n")