size = int(input())

racing_number = input()

race_route, tunnel_positions = [], []
final_position = tuple()
car_position = (0, 0)

for row in range(size):
    race_route.append(input().split())

    if "T" in race_route[row]:
        tunnel_positions.append((row, race_route[row].index("T")))

    if "F" in race_route[row]:
        final_position = (row, race_route[row].index("F"))

total_kilometers = 0

directions = {
    "up": lambda x: (x[0] - 1, x[1]),
    "down": lambda x: (x[0] + 1, x[1]),
    "left": lambda x: (x[0], x[1] - 1),
    "right": lambda x: (x[0], x[1] + 1),
}

direction = input()

while direction != "End":
    car_position = directions[direction](car_position)

    total_kilometers += 10

    if car_position == final_position:
        print(f"Racing car {racing_number} finished the stage!")
        break

    elif car_position in tunnel_positions:
        tunnel_positions.remove(car_position)
        race_route[car_position[0]][car_position[1]] = "."
        car_position = tunnel_positions.pop()
        race_route[car_position[0]][car_position[1]] = "."
        total_kilometers += 20

    direction = input()

else:
    print(f"Racing car {racing_number} DNF.")

print(f"Distance covered {total_kilometers} km.")
race_route[car_position[0]][car_position[1]] = "C"
[print("".join(row)) for row in race_route]
