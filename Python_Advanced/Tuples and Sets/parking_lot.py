cars = set()

for _ in range(int(input())):
    command, car_number = input().split(", ")

    if command == "IN":
        cars.add(car_number)
    elif command == "OUT":
        cars.remove(car_number)

if cars:
    print(*cars, sep="\n")
else:
    print("Parking Lot is Empty")