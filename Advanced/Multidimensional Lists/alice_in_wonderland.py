size = int(input())

territory = []
alice_position = []

for row in range(size):
    territory.append(input().split())

    if "A" in territory[row]:
        alice_position = [row, territory[row].index("A")]
        territory[alice_position[0]][alice_position[1]] = "*"


moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

collected_tea_bags = 0

while True:
    move = input()
    move_row, move_col = moves[move]

    move_row += alice_position[0]
    move_col += alice_position[1]

    if move_row < 0 or move_row >= size or move_col < 0 or move_col >= size:
        break

    current_element = territory[move_row][move_col]
    territory[move_row][move_col] = "*"

    if current_element == "R":
        break

    alice_position = [move_row, move_col]

    if current_element.isdigit():
        collected_tea_bags += int(current_element)

        if collected_tea_bags >= 10:
            break

if collected_tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

[print(*row, sep=" ") for row in territory]