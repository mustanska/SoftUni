routes = input().split("||")
fuel = int(input())
ammunition = int(input())

is_failed = False

for route in routes:
    command_data = route.split()
    command = command_data[0]

    if command == "Travel":
        light_years = int(command_data[1])
        for year in range(1, light_years + 1):
            fuel -= 1

            if fuel < 0:
                is_failed = True
                break
        else:
            print(f"The spaceship travelled {light_years} light-years.")

    elif command == "Enemy":
        armour = int(command_data[1])
        if ammunition >= armour:
            for num in range(1, armour + 1):
                ammunition -= 1
            print(f"An enemy with {armour} armour is defeated.")

        else:
            for num in range(1, armour + 1):
                fuel -= 2
                if fuel < 0:
                    is_failed = True
                    break
            else:
                print(f"An enemy with {armour} armour is outmaneuvered.")

    elif command == "Repair":
        added_amount = int(command_data[1])
        fuel += added_amount
        ammunition += added_amount * 2

        print(f"Ammunitions added: {added_amount * 2}.")
        print(f"Fuel added: {added_amount}.")

    elif command == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break

    if is_failed:
        print("Mission failed.")
        break
