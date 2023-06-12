from collections import deque

milligrams_of_caffeine = deque([int(x) for x in input().split(", ")])
energy_drinks = deque([int(x) for x in input().split(", ")])

maximum_caffeine = 300
stamat_caffeine = 0

while milligrams_of_caffeine and energy_drinks:
    milligram_of_caffeine = milligrams_of_caffeine.pop()
    energy_drink = energy_drinks.popleft()

    caffeine = milligram_of_caffeine * energy_drink

    if caffeine + stamat_caffeine <= maximum_caffeine:
        stamat_caffeine += caffeine
    else:
        energy_drinks.append(energy_drink)
        stamat_caffeine = max(stamat_caffeine - 30, 0)


if energy_drinks:
    print(f"Drinks left: {', '.join([str(el) for el in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamat_caffeine} mg caffeine.")
