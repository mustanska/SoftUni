from collections import deque

number_of_pumps = int(input())
pumps = deque()

for _ in range(number_of_pumps):
    pumps.append([int(value) for value in input().split()])

fuel_in_tank = 0
pump_number = 0
pumps_copy = pumps.copy()

while pumps_copy:
    petrol, distance = pumps_copy.popleft()
    fuel_in_tank += petrol

    if fuel_in_tank < distance:
        pumps.rotate(-1)
        pumps_copy = pumps.copy()
        pump_number += 1
        fuel_in_tank = 0
    else:
        fuel_in_tank -= distance

print(pump_number)