rows, cols = [int(x) for x in input().split()]

playground = []
my_position = tuple()
players_positions = []

for row in range(rows):
    playground.append(input().split())

    if "B" in playground[row]:
        my_position = (row, playground[row].index("B"))
        playground[my_position[0]][my_position[1]] = "-"

    columns = [i for i, x in enumerate(playground[row]) if x == "P"]
    for column in columns:
        players_positions.append((row, column))

directions = {
    "up": lambda x: (x[0] - 1, x[1]) if 0 <= x[0] - 1 < rows and playground[x[0] - 1][x[1]] != "O" else x,
    "down": lambda x: (x[0] + 1, x[1]) if 0 <= x[0] + 1 < rows and playground[x[0] + 1][x[1]] != "O" else x,
    "left": lambda x: (x[0], x[1] - 1) if 0 <= x[1] - 1 < cols and playground[x[0]][x[1] - 1] != "O" else x,
    "right": lambda x: (x[0], x[1] + 1) if 0 <= x[1] + 1 < cols and playground[x[0]][x[1] + 1] != "O" else x,
}

command = input()

moves = 0
touched_opponents = 0

while command != "Finish":
    position = directions[command](my_position)

    if my_position != position:
        my_position = position

        moves += 1

        if my_position in players_positions:
            players_positions.remove(my_position)
            touched_opponents += 1
            playground[my_position[0]][my_position[1]] = "-"

        if not players_positions:
            break

    command = input()

print(f"Game over!\nTouched opponents: {touched_opponents} Moves made: {moves}")
