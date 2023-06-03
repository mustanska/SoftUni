FOOD_QUANTITY = 10

size = int(input())
territory = [list(input()) for _ in range(size)]

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

snake_position = []
burrows = []

for row in range(size):
    for col in range(size):
        if territory[row][col] == "S":
            snake_position.extend([row, col])
            territory[row][col] = "."

        elif territory[row][col] == "B":
            burrows.append([row, col])

total_food = 0

while total_food < FOOD_QUANTITY:
    command = input()

    move_row, move_col = moves[command]
    move_row += snake_position[0]
    move_col += snake_position[1]

    if not (0 <= move_row < size and 0 <= move_col < size):
        print("Game over!")
        break

    if territory[move_row][move_col] == "*":
        total_food += 1

    elif territory[move_row][move_col] == "B":
        territory[move_row][move_col] = "."
        burrows.remove([move_row, move_col])
        move_row, move_col = burrows[0]

    territory[move_row][move_col] = "."
    snake_position = [move_row, move_col]

else:
    print("You won! You fed the snake.")
    territory[snake_position[0]][snake_position[1]] = "S"

print(f"Food eaten: {total_food}")
[print("".join(row)) for row in territory]