from collections import deque

chocolates = deque(int(x) for x in input().split(", "))
cups_of_milk = deque(int(x) for x in input().split(", "))

milkshakes = 0

while milkshakes < 5 and chocolates and cups_of_milk:
    chocolate = chocolates.pop()
    cup = cups_of_milk.popleft()

    if chocolate <= 0 and cup <= 0:
        continue

    if cup <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate <= 0:
        cups_of_milk.appendleft(cup)
        continue

    if cup == chocolate:
        milkshakes += 1
    else:
        chocolates.append(chocolate - 5)
        cups_of_milk.append(cup)

if milkshakes < 5:
    print("Not enough milkshakes.")
else:
    print("Great! You made all the chocolate milkshakes needed!")

print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups_of_milk) or 'empty'}")