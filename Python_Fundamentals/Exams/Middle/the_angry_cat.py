price_rating = [int(x) for x in input().split(", ")]
entry_point = int(input())
item_types = input()

left_damage = 0
right_damage = 0

for i in range(len(price_rating)):
    if i == entry_point:
        value = price_rating[entry_point]
        if item_types == "cheap":
            left_damage = sum([x for x in (price_rating[0:entry_point]) if x < value])
            right_damage = sum([x for x in (price_rating[entry_point + 1:]) if x < value])

        elif item_types == "expensive":
            left_damage = sum([x for x in (price_rating[0:entry_point]) if x >= value])
            right_damage = sum([x for x in (price_rating[entry_point + 1:]) if x >= value])

if left_damage >= right_damage:
    print(f"")
