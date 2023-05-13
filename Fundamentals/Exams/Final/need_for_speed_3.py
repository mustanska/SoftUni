number_of_cars = int(input())

cars = {}

for _ in range(number_of_cars):
    car_info = input().split("|")
    car_type = car_info[0]
    mileage = int(car_info[1])
    fuel = int(car_info[2])

    cars[car_type] = {"mileage": mileage, "fuel": fuel}

while True:
    line = input()

    if line == "Stop":
        break

    line = line.split(" : ")
    command = line[0]
    car = line[1]

    if command == "Drive":
        distance = int(line[2])
        fuel = int(line[3])

        if cars[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["fuel"] -= fuel
            cars[car]["mileage"] += distance

            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

        if cars[car]["mileage"] > 100000:
            print(f"Time to sell the {car}!")
            del cars[car]

    if command == "Refuel":
        fuel = int(line[2])

        current_fuel = cars[car]["fuel"]
        cars[car]["fuel"] = min(75, current_fuel + fuel)

        print(f"{car} refueled with {cars[car]['fuel'] - current_fuel} liters")

    if command == "Revert":
        km = int(line[2])

        if cars[car]["mileage"] - km < 10000:
            cars[car]["mileage"] = 10000
        else:
            cars[car]["mileage"] -= km
            print(f"{car} mileage decreased by {km} kilometers")

for car, info in cars.items():
    print(f"{car} -> Mileage: {info['mileage']} kms, Fuel in the tank: {info['fuel']} lt.")