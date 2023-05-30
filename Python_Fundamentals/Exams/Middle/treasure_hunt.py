chest = input().split("|")

stolen_loots = []

while chest:
    line = input()

    if line == "Yohoho!":
        sum_length = sum([len(el) for el in chest])
        average_gain = sum_length / len(chest)
        print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
        break

    command_data = line.split()
    command = command_data[0]

    if command == "Loot":
        for i in range(1, len(command_data)):
            if not command_data[i] in chest:
                chest.insert(0, command_data[i])

    elif command == "Drop":
        index = int(command_data[1])

        if index in range(len(chest)):
            element = chest[index]
            chest.pop(index)
            chest.append(element)

    elif command == "Steal":
        count = int(command_data[1])

        if count < len(chest):
            stolen_loots = [chest[i] for i in range(len(chest) - count, len(chest))]
        else:
            stolen_loots = chest.copy()

        print(*stolen_loots, sep=", ")

        for element in stolen_loots:
            if element in chest:
                chest.remove(element)
else:
    print("Failed treasure hunt.")

