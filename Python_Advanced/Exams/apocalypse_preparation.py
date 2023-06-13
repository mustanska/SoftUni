from collections import deque


def find_key(given_sum, given_dict):
    keys = list(given_dict.keys())
    values = list(given_dict.values())

    return keys[values.index(given_sum)]


def add_created_items(given_item):
    if given_item not in created_items:
        created_items[given_item] = 0
    created_items[given_item] += 1


textiles = deque([int(x) for x in input().split()])
medicaments = deque([int(x) for x in input().split()])

healing_items = {
    "Patch": 30,
    "Bandage": 40,
    "MedKit": 100,
}

created_items = {}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()

    current_sum = textile + medicament

    if current_sum in healing_items.values():
        item = find_key(current_sum, healing_items)

        add_created_items(item)

    elif current_sum > max(healing_items.values()):
        max_sum = max(healing_items.values())
        item = find_key(max_sum, healing_items)

        add_created_items(item)

        remaining_resource = current_sum - max_sum
        medicaments.append(medicaments.pop() + remaining_resource)

    else:
        medicaments.append(medicament + 10)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
else:
    if not textiles:
        print("Textiles are empty.")

    if not medicaments:
        print("Medicaments are empty.")

for item, count in sorted(created_items.items(), key=lambda x: (-x[1], x[0])):
    print(f"{item} - {count}")

if medicaments:
    print(f"Medicaments left: {', '.join([str(el) for el in reversed(medicaments)])}")

if textiles:
    print(f"Textiles left: {', '.join([str(el) for el in textiles])}")
