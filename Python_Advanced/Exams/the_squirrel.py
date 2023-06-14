size = int(input())
moves = input().split(", ")

field = []
squirrel_position = tuple()
hazelnuts_positions = []

for row in range(size):
    field.append(list(input()))

    if "s" in field[row]:
        squirrel_position = (row, field[row].index("s"))

    hazelnuts_columns = [i for i, x in enumerate(field[row]) if x == "h"]

    for column in hazelnuts_columns:
        hazelnuts_positions.append((row, column))

total_hazelnut = 0

directions = {
    "up": lambda x: (x[0] - 1, x[1]),
    "down": lambda x: (x[0] + 1, x[1]),
    "left": lambda x: (x[0], x[1] - 1),
    "right": lambda x: (x[0], x[1] + 1),
}

for move in moves:
    squirrel_position = directions[move](squirrel_position)

    if not (0 <= squirrel_position[0] < size and 0 <= squirrel_position[1] < size):
        print("The squirrel is out of the field.")
        break

    if field[squirrel_position[0]][squirrel_position[1]] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break

    if squirrel_position in hazelnuts_positions:
        hazelnuts_positions.remove(squirrel_position)
        total_hazelnut += 1
        field[squirrel_position[0]][squirrel_position[1]] = "*"

        if not hazelnuts_positions:
            print("Good job! You have collected all hazelnuts!")
            break

else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {total_hazelnut}")
