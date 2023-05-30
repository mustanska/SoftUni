number_of_plants = int(input())

plants = {}

for _ in range(number_of_plants):
    plant_info = input().split("<->")
    plant = plant_info[0]
    rarity = plant_info[1]

    plants[plant] = {"rarity": rarity, "rating": []}

while True:
    line = input()

    if line == "Exhibition":
        break

    line = line.split(": ")
    command = line[0]
    info = line[1]
    info = info.split(" - ")
    plant = info[0]

    if plant not in plants:
        print("error")
        continue

    if command == "Rate":
        rating = int(info[1])
        plants[plant]["rating"].append(rating)

    elif command == "Update":
        rarity = info[1]
        plants[plant]["rarity"] = rarity

    elif command == "Reset":
        plants[plant]["rating"].clear()

print("Plants for the exhibition:")
for plant, info in plants.items():
    if info["rating"]:
        avg_rating = sum(info["rating"]) / len(info["rating"])
    else:
        avg_rating = 0
    print(f"- {plant}; Rarity: {info['rarity']}; Rating: {avg_rating:.2f}")
