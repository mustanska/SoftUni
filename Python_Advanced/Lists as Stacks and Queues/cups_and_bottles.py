from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = deque([int(x) for x in input().split()])

wasted_water = 0

while cups and bottles:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()

    if current_cup <= current_bottle:
        wasted_water += current_bottle - current_cup
    else:
        cups.appendleft(current_cup - current_bottle)

if cups:
    print("Cups:", end=" ")
    print(*cups, sep=" ")

if bottles:
    print("Bottles:", end=" ")
    print(*bottles, sep=" ")

print(f"Wasted litters of water: {wasted_water}")