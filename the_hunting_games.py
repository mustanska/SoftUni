days = int(input())
players = int(input())
energy = float(input())
water_for_one = float(input())
food_for_one = float(input())

total_water = days * players * water_for_one
total_food = days * players * food_for_one

for day in range(1, days + 1):
    energy_loss = float(input())

    energy -= energy_loss

    if energy <= 0:
        print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
        break

    if day % 2 == 0:
        energy *= 1.05
        total_water *= 0.7

    if day % 3 == 0:
        energy *= 1.1
        total_food -= total_food / players


if energy > 0:
    print(f"You are ready for the quest. You will be left with - {energy:.2f} energy!")