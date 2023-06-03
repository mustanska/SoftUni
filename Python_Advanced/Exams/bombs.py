from collections import deque

bomb_effects = deque([int(el) for el in input().split(", ")])
bomb_casing = deque([int(el) for el in input().split(", ")])

materials_for_bombs = {
    "Datura Bombs": 40,
    "Cherry Bombs": 60,
    "Smoke Decoy Bombs": 120,
}

created_bombs_count = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0,
}

while bomb_casing and bomb_effects:
    if all([value >= 3 for value in created_bombs_count.values()]):
        print("Bene! You have successfully filled the bomb pouch!")
        break

    effect = bomb_effects.popleft()
    casing = bomb_casing.pop()

    for key, value in materials_for_bombs.items():
        if effect + casing == value:
            created_bombs_count[key] += 1
            break
    else:
        bomb_casing.append(casing - 5)
        bomb_effects.appendleft(effect)

else:
    print("You don't have enough materials to fill the bomb pouch.")

print(f"Bomb Effects: {', '.join([str(el) for el in bomb_effects]) if bomb_effects else 'empty'}")
print(f"Bomb Casings: {', '.join([str(el) for el in bomb_casing]) if bomb_casing else 'empty'}")
[print(f"{key}: {value}") for key, value in sorted(created_bombs_count.items())]