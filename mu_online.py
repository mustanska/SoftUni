rooms = input().split("|")

MAX_HEALTH = 100
current_health = MAX_HEALTH
bitcoins = 0

for num_room, room in enumerate(rooms, start=1):
    command, number_as_str = room.split()
    number = int(number_as_str)

    if command == "potion":
        amount = min(number, MAX_HEALTH - current_health)
        current_health = min(current_health + number, MAX_HEALTH)

        print(f"You healed for {amount} hp.")
        print(f"Current health: {current_health} hp.")

    elif command == "chest":
        bitcoins += number

        print(f"You found {number} bitcoins.")

    else:
        current_health -= number

        if current_health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {num_room}")
            exit(0)

print("You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {current_health}")