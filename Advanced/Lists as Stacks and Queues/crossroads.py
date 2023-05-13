from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

cars = deque()
cars_passed = 0

while True:
    line = input()

    if line == "END":
        print("Everyone is safe.")
        print(f"{cars_passed} total cars passed the crossroads.")
        break

    if line == "green":
        green_on = green_light_duration

        while cars and green_on > 0:
            car = cars.popleft()

            time = green_on + free_window_duration

            if len(car) > time:
                print("A crash happened!")
                print(f"{car} was hit at {car[time]}.")
                exit()

            green_on -= len(car)
            cars_passed += 1
    else:
        cars.append(line)
