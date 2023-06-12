def forecast(*args):
    weathers_locations = {}
    weathers = ["Sunny", "Cloudy", "Rainy"]

    for location, weather in args:
        weathers_locations[location] = weather

    result = ""

    for location, weather in sorted(weathers_locations.items(), key=lambda x: (weathers.index(x[1]), x[0])):
        result += f"{location} - {weather}\n"

    return result


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
