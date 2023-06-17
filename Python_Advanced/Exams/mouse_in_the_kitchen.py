rows, cols = [int(x) for x in input().split(",")]

cupboard = []
mouse_position = []
total_cheeses = 0

for row in range(rows):
    cupboard.append(list(input()))

    if "M" in cupboard[row]:
        mouse_position.extend([row, cupboard[row].index("M")])
        cupboard[mouse_position[0]][mouse_position[1]] = "*"

    if "C" in cupboard[row]:
        total_cheeses += cupboard[row].count("C")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

direction = input()

while direction != "danger":
    current_row = mouse_position[0] + directions[direction][0]
    current_col = mouse_position[1] + directions[direction][1]

    if not(0 <= current_row < rows and 0 <= current_col < cols):
        print("No more cheese for tonight!")
        break

    if cupboard[current_row][current_col] == "@":
        direction = input()
        continue

    mouse_position = [current_row, current_col]

    if cupboard[current_row][current_col] == "T":
        print("Mouse is trapped!")
        break

    if cupboard[current_row][current_col] == "C":
        cupboard[current_row][current_col] = "*"
        total_cheeses -= 1

        if not total_cheeses:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    direction = input()

else:
    print("Mouse will come back later!")

cupboard[mouse_position[0]][mouse_position[1]] = "M"
[print(*row, sep="") for row in cupboard]
