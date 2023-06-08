from collections import deque


def find_new_sum_of_gift(gift_material, gift_magic, value):
    if value < 100:
        if value % 2 == 0:
            gift_material *= 2
            gift_magic *= 3
            value = gift_magic + gift_material

        else:
            value *= 2

    elif value >= 500:
        value /= 2

    return value


def check_for_gifts(value):
    for gift, gift_range in gifts_range.items():
        if gift_range(value):
            gifts_made[gift] += 1
            return True
    return False


materials = deque([int(x) for x in input().split()])
magic_levels = deque([int(x) for x in input().split()])

gifts_range = {
    "Gemstone": lambda x: 100 <= x < 200,
    "Porcelain Sculpture": lambda x: 200 <= x < 300,
    "Gold": lambda x: 300 <= x < 400,
    "Diamond Jewellery": lambda x: 400 <= x < 500,
}

gifts_made = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0,
}

while materials and magic_levels:
    material = materials.pop()
    magic_level = magic_levels.popleft()

    sum_gift = material + magic_level

    if not check_for_gifts(sum_gift):
        sum_gift = find_new_sum_of_gift(material, magic_level, sum_gift)
        check_for_gifts(sum_gift)

if (gifts_made["Gemstone"] and gifts_made["Porcelain Sculpture"]) or \
        (gifts_made["Gold"] and gifts_made["Diamond Jewellery"]):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(el) for el in materials])}")

if magic_levels:
    print(f"Magic left: {', '.join([str(el) for el in magic_levels])}")

for gift_name, gift_count in sorted(gifts_made.items()):
    if gift_count:
        print(f"{gift_name}: {gift_count}")
