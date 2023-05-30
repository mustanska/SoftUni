number_of_heroes = int(input())

heroes = {}

for _ in range(number_of_heroes):
    heroes_info = input().split()
    name = heroes_info[0]
    hit_points = int(heroes_info[1])
    mana_points = int(heroes_info[2])

    heroes[name] = {"HP": hit_points, "MP": mana_points}

while True:
    line = input()

    if line == "End":
        break

    line = line.split(" - ")
    command = line[0]
    hero_name = line[1]

    if command == "CastSpell":
        mp_need = int(line[2])
        spell_name = line[3]

        if heroes[hero_name]["MP"] < mp_need:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
        else:
            heroes[hero_name]["MP"] -= mp_need
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MP']} MP!")

    elif command == "TakeDamage":
        damage = int(line[2])
        attacker = line[3]

        if heroes[hero_name]["HP"] <= damage:
            del heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
        else:
            heroes[hero_name]["HP"] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")

    elif command == "Recharge":
        amount = int(line[2])

        old_amount = heroes[hero_name]["MP"]
        heroes[hero_name]["MP"] = min(200, old_amount + amount)
        print(f"{hero_name} recharged for {heroes[hero_name]['MP'] - old_amount} MP!")

    elif command == "Heal":
        amount = int(line[2])

        old_amount = heroes[hero_name]["HP"]
        heroes[hero_name]["HP"] = min(100, old_amount + amount)
        print(f"{hero_name} healed for {heroes[hero_name]['HP'] - old_amount} HP!")

for name, values in heroes.items():
    print(f"{name}")
    for key, value in values.items():
        print(f"{key}: {value}")
