from collections import deque

clothes = deque([int(garment) for garment in input().split()])
rack_capacity = int(input())

racks = 1
current_capacity = rack_capacity

while clothes:
    garment = clothes.pop()

    if garment <= current_capacity:
        current_capacity -= garment
    else:
        racks += 1
        current_capacity = rack_capacity - garment

print(racks)
