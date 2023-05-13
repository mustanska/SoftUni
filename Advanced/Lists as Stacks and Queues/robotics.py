from collections import deque
from datetime import datetime, timedelta

robots_data = input().split(";")
robots = {}
products = deque()

for robot in robots_data:
    name, secs = robot.split("-")
    robots[name] = [int(secs), 0]

starting_time = datetime.strptime(input(), "%H:%M:%S")

while True:
    product = input()

    if product == "End":
        break

    products.append(product)

while products:
    starting_time += timedelta(0, 1)

    free_robots = deque()

    for name, data in robots.items():
        if data[1] > 0:
            robots[name][1] -= 1

        if data[1] == 0:
            free_robots.append(name)

    if free_robots:
        robot = free_robots.popleft()
        product = products.popleft()
        robots[robot][1] = robots[robot][0]
        print(f"{robot} - {product} [{starting_time.strftime('%H:%M:%S')}]")
    else:
        products.rotate(-1)
