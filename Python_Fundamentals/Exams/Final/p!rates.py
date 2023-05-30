cities = {}

while True:
    line = input()

    if line == "Sail":
        break

    line = line.split("||")
    city = line[0]
    population = int(line[1])
    gold = int(line[2])

    if city not in cities:
        cities[city] = {"population": population, "gold": gold}
    else:
        cities[city]["population"] += population
        cities[city]["gold"] += gold

while True:
    line = input()

    if line == "End":
        break

    line = line.split("=>")
    command = line[0]
    city = line[1]

    if command == "Plunder":
        people = int(line[2])
        gold = int(line[3])

        cities[city]["population"] -= people
        cities[city]["gold"] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")

        if cities[city]["population"] == 0 or cities[city]["gold"] == 0:
            del cities[city]
            print(f"{city} has been wiped off the map!")

    elif command == "Prosper":
        gold = int(line[2])

        if gold < 0:
            print("Gold added cannot be a negative number!")
            continue

        cities[city]["gold"] += gold
        print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, value in cities.items():
        print(f"{city} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")