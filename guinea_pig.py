quantity_of_food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
pig_weight = float(input()) * 1000

for day in range(1, 31):
    quantity_of_food -= 300

    if day % 2 == 0:
        hay -= quantity_of_food * 0.05

    if day % 3 == 0:
        cover -= 1/3 * pig_weight

    if quantity_of_food <= 0 or hay <= 0 or cover <= 0:
        print("Merry must go to the pet store!")
        break

if quantity_of_food > 0 and hay > 0 and cover > 0:
    quantity_of_food = quantity_of_food / 1000
    hay = hay / 1000
    cover = cover / 1000
    print(f"Everything is fine! Puppy is happy! Food: {quantity_of_food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")