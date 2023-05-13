initial_energy = int(input())
battle = 0

while True:
    line = input()

    if line == "End of battle":
        print(f"Won battles: {battle}. Energy left: {initial_energy}")
        break

    distance = int(line)

    if initial_energy - distance >= 0:
        initial_energy -= distance
        battle += 1
    else:
        print(f"Not enough energy! Game ends with {battle} won battles and {initial_energy} energy")
        break

    if battle % 3 == 0:
        initial_energy += battle

