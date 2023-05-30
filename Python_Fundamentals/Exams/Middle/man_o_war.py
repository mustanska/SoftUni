def is_valid_index(ship_list, idx):
    if 0 <= idx < len(ship_list):
        return True
    return False


pirate_ship = [int(status) for status in input().split(">")]
warship = [int(status) for status in input().split(">")]
max_health = int(input())

while True:
    line = input()

    if line == "Retire":
        print(f"Pirate ship status: {sum(pirate_ship)}")
        print(f"Warship status: {sum(warship)}")
        break

    command_data = line.split()
    command = command_data[0]

    if command == "Fire":
        index = int(command_data[1])
        damage = int(command_data[2])

        if is_valid_index(warship, index):
            warship[index] -= damage

            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                break

    elif command == "Defend":
        start_index = int(command_data[1])
        end_index = int(command_data[2])
        damage = int(command_data[3])

        if is_valid_index(pirate_ship, start_index) and is_valid_index(pirate_ship, end_index):
            for index in range(start_index, end_index + 1):
                pirate_ship[index] -= damage

                if pirate_ship[index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit(0)

    elif command == "Repair":
        index = int(command_data[1])
        given_health = int(command_data[2])

        if is_valid_index(pirate_ship, index):
            pirate_ship[index] = min(pirate_ship[index] + given_health, max_health)

    elif command == "Status":
        count_for_repair = 0
        for status in pirate_ship:
            if status < max_health * 0.2:
                count_for_repair += 1
        print(f"{count_for_repair} sections need repair.")

