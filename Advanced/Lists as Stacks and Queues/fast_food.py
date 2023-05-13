from collections import deque

quantity_of_food = int(input())
orders = deque([int(order) for order in input().split()])

print(max(orders))

while orders:
    current_order = orders.popleft()
    if current_order <= quantity_of_food:
        quantity_of_food -= current_order
    else:
        orders.appendleft(current_order)
        print("Orders left:", end=" ")
        print(*orders, sep=" ")
        break
else:
    print("Orders complete")
