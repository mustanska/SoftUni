from collections import deque
queue = deque()

quantity_of_water = int(input())

while True:
    name = input()

    if name == "Start":
        break

    queue.append(name)

while True:
    command = input()

    if command == "End":
        print(f"{quantity_of_water} liters left")
        break

    if len(command.split()) == 1:
        litters = int(command)

        if litters <= quantity_of_water:
            quantity_of_water -= litters
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")

    else:
        filled_litters = int(command.split()[1])
        quantity_of_water += filled_litters

