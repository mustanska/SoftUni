SIZE = 6

field, rover_position = [], []

for row in range(SIZE):
    field.append(input().split())

    if "E" in field[row]:
        rover_position.extend([row, field[row].index("E")])

commands = input().split(", ")

directions = {
    "up": lambda x, y: [x - 1, y] if 0 <= x - 1 < SIZE else [SIZE - 1, y],
    "down": lambda x, y: [x + 1, y] if 0 <= x + 1 < SIZE else [0, y],
    "left": lambda x, y: [x, y - 1] if 0 <= y - 1 < SIZE else [x, SIZE - 1],
    "right": lambda x, y: [x, y + 1] if 0 <= y + 1 < SIZE else [x, 0],
}

deposits = {"W": False, "M": False, "C": False}
deposits_names = {"W": "Water", "M": "Metal", "C": "Concrete"}

for command in commands:
    rover_position = directions[command](*rover_position)
    current_element = field[rover_position[0]][rover_position[1]]

    if current_element in deposits:
        deposits[current_element] = True
        print(f"{deposits_names[current_element]} deposit found at ({rover_position[0]}, {rover_position[1]})")

    elif current_element == "R":
        print(f"Rover got broken at ({rover_position[0]}, {rover_position[1]})")
        break

if all(deposits.values()):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")