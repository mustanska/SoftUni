from collections import deque

fireworks_effects = deque([int(x) for x in input().split(", ")])
explosive_power = deque([int(x) for x in input().split(", ")])

firework_types = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0,
}

while fireworks_effects and explosive_power:
    if all([value >= 3 for value in firework_types.values()]):
        break

    effect = fireworks_effects.popleft()
    power = explosive_power.pop()

    if effect <= 0:
        explosive_power.append(power)
        continue

    if power <= 0:
        fireworks_effects.appendleft(effect)
        continue

    firework_sum = effect + power

    if firework_sum % 3 == 0 and firework_sum % 5 != 0:
        firework_types["Palm Fireworks"] += 1
        continue

    elif firework_sum % 5 == 0 and firework_sum % 3 != 0:
        firework_types["Willow Fireworks"] += 1
        continue

    elif firework_sum % 5 == 0 and firework_sum % 3 == 0:
        firework_types["Crossette Fireworks"] += 1
        continue

    fireworks_effects.append(effect - 1)
    explosive_power.append(power)

if all([value >= 3 for value in firework_types.values()]):
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks_effects:
    print(f"Firework Effects left: {', '.join([str(el) for el in fireworks_effects])}")

if explosive_power:
    print(f"Explosive Power left: {', '.join([str(el) for el in explosive_power])}")

for key, value in firework_types.items():
    print(f"{key}: {value}")
