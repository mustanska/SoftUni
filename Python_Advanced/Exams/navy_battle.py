size = int(input())

battlefield = []
submarine_position = tuple()
total_cruisers = 0

for row in range(size):
    battlefield.append(list(input()))

    if "S" in battlefield[row]:
        submarine_position = (row, battlefield[row].index("S"))
        battlefield[submarine_position[0]][submarine_position[1]] = "-"

    if "C" in battlefield[row]:
        total_cruisers += battlefield[row].count("C")

directions = {
    "up": lambda x: (x[0] - 1, x[1]),
    "down": lambda x: (x[0] + 1, x[1]),
    "left": lambda x: (x[0], x[1] - 1),
    "right": lambda x: (x[0], x[1] + 1),
}

total_hits = 0
destroyed_cruisers = 0

while total_hits < 3 and destroyed_cruisers < total_cruisers:
    direction = input()

    submarine_position = directions[direction](submarine_position)

    if battlefield[submarine_position[0]][submarine_position[1]] == "*":
        total_hits += 1

    elif battlefield[submarine_position[0]][submarine_position[1]] == "C":
        destroyed_cruisers += 1

    battlefield[submarine_position[0]][submarine_position[1]] = "-"

battlefield[submarine_position[0]][submarine_position[1]] = "S"

if total_hits == 3:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_position[0]}, {submarine_position[1]}]!")
else:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

[print(*row, sep="") for row in battlefield]
