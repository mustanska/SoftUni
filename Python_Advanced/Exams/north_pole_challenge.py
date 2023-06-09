def make_moves(move_direction, move_steps, items):
    move_row, move_col = directions[move_direction]

    current_row, current_col = my_position

    for _ in range(move_steps):
        current_row = check_index(current_row + move_row, rows)
        current_col = check_index(current_col + move_col, cols)

        if workshop[current_row][current_col] == "D":
            collected_items["Christmas decorations"] += 1
            items -= 1

        elif workshop[current_row][current_col] == "C":
            collected_items["Cookies"] += 1
            items -= 1

        elif workshop[current_row][current_col] == "G":
            collected_items["Gifts"] += 1
            items -= 1

        workshop[current_row][current_col] = "x"

        if not items:
            break

    return [current_row, current_col], items


def check_index(index, range_size):
    if index < 0:
        return range_size - 1

    elif index >= range_size:
        return 0

    else:
        return index


rows, cols = [int(x) for x in input().split(", ")]

workshop = []
my_position = []
total_items = 0

for row in range(rows):
    workshop.append(input().split())

    for col in range(cols):
        current_element = workshop[row][col]
        if current_element.isalpha():
            if current_element == "Y":
                my_position.extend([row, col])
                workshop[row][col] = "x"
            else:
                total_items += 1

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0),
}

collected_items = {
    "Christmas decorations": 0,
    "Gifts": 0,
    "Cookies": 0,
}

command = input()

while command != "End":
    direction, steps = command.split("-")

    result = make_moves(direction, int(steps), total_items)
    my_position, total_items = result

    if not total_items:
        print("Merry Christmas!")
        break

    command = input()

workshop[my_position[0]][my_position[1]] = "Y"
print("You've collected:")
[print(f"- {value} {key}") for key, value in collected_items.items()]
[print(*row, sep=" ") for row in workshop]
