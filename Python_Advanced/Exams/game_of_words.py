def player_move(move, position, text):
    move_row, move_col = moves[move]
    move_row += position[0]
    move_col += position[1]

    if not(0 <= move_row < size and 0 <= move_col < size):
        text = text[:-1]

    else:
        position_content = field[move_row][move_col]

        if position_content.isalpha():
            text += position_content
            field[move_row][move_col] = "-"

        position = [move_row, move_col]

    return text, position


string = input()

size = int(input())

field = []
player_position = []

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    field.append(list(input()))

    if "P" in field[row]:
        player_position.extend([row, field[row].index("P")])
        field[row][field[row].index("P")] = "-"

for _ in range(int(input())):
    command = input()

    result = player_move(command, player_position, string)

    string = result[0]
    player_position = result[1]

field[player_position[0]][player_position[1]] = "P"
print(string)
[print("".join(row)) for row in field]
