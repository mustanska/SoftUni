def move(santa_move, position):
    move_row, move_col = moves[santa_move]
    current_row = position[0] + move_row
    current_col = position[1] + move_col

    if 0 <= current_row < size and 0 <= current_col < size:
        return [current_row, current_col]

    return position


def give_presents(position, presents, nice_kids):
    for row in range(size):
        for col in range(size):
            if position[0] == row and position[1] == col:
                if neighborhood[row][col] == "V" and nice_kids < total_nice_kids:
                    presents -= 1
                    nice_kids += 1

                elif neighborhood[row][col] == "C":
                    for move_row, move_col in moves.values():
                        neighbor_row = move_row + row
                        neighbor_col = move_col + col

                        if presents:
                            if neighborhood[neighbor_row][neighbor_col] == "V" and nice_kids < total_nice_kids:
                                nice_kids += 1
                                presents -= 1

                            elif neighborhood[neighbor_row][neighbor_col] == "X":
                                presents -= 1

                            neighborhood[neighbor_row][neighbor_col] = "-"

                neighborhood[row][col] = "-"

                return presents, nice_kids


presents_count = int(input())

size = int(input())

neighborhood = []
santa_position = []
total_nice_kids = 0
happy_nice_kids = 0

moves = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0),
}

for row in range(size):
    neighborhood.append(input().split())

    for col in range(size):
        if neighborhood[row][col] == "S":
            santa_position.extend([row, col])
            neighborhood[row][col] = "-"

        if neighborhood[row][col] == "V":
            total_nice_kids += 1

while presents_count:
    command = input()

    if command == "Christmas morning":
        break

    santa_position = move(command, santa_position)

    result = give_presents(santa_position, presents_count, happy_nice_kids)

    if result:
        presents_count = result[0]
        happy_nice_kids = result[1]

        if happy_nice_kids == total_nice_kids:
            break

else:
    print("Santa ran out of presents!")

neighborhood[santa_position[0]][santa_position[1]] = "S"
[print(*row, sep=" ") for row in neighborhood]

if happy_nice_kids < total_nice_kids:
    print(f"No presents for {total_nice_kids - happy_nice_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")