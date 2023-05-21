def player_move(position, move_direction, steps_move):
    move_row, move_col = moves[move_direction](steps_move)

    current_row = move_row + position[0]
    current_col = move_col + position[1]

    if current_row < 0 or current_col < 0 or current_row > SIZE - 1 or current_col > SIZE - 1:
        return position

    if shotgun_range[current_row][current_col] == "x":
        return position

    return [current_row, current_col]


def player_shoot(position, shoot_direction):
    shoot_row, shoot_col = moves[shoot_direction](1)
    current_row, current_col = position

    while True:
        current_row += shoot_row
        current_col += shoot_col

        if not (0 <= current_row < SIZE and 0 <= current_col < SIZE):
            break

        if shotgun_range[current_row][current_col] == "x":
            return [current_row, current_col]


SIZE = 5

moves = {
    "up": lambda x: (-1 * x, 0),
    "down": lambda x: (1 * x, 0),
    "left": lambda x: (0, -1 * x),
    "right": lambda x: (0, 1 * x),
}

shotgun_range = []
player_position = []
total_targets = 0
shooting_targets = []

for row in range(SIZE):
    shotgun_range.append(input().split())

    if "x" in shotgun_range[row]:
        total_targets += shotgun_range[row].count("x")

    if "A" in shotgun_range[row]:
        player_position.extend([row, shotgun_range[row].index("A")])
        shotgun_range[row][shotgun_range[row].index("A")] = "."

for _ in range(int(input())):
    command, *command_data = input().split()
    direction = command_data[0]

    if command == "move":
        steps = int(command_data[1])
        player_position = player_move(player_position, direction, steps)

    elif command == "shoot":
        result = player_shoot(player_position, direction)

        if not result:
            continue

        shooting_targets.append(result)
        shotgun_range[result[0]][result[1]] = "."

        if len(shooting_targets) == total_targets:
            print(f"Training completed! All {total_targets} targets hit.")
            break
else:
    print(f"Training not completed! {total_targets - len(shooting_targets)} targets left.")

print(*shooting_targets, sep="\n")

