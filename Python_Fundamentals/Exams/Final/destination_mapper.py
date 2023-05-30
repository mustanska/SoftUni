import re

string = input()

pattern = r"([=\/])([A-Z][A-Za-z]{2,})\1"
matches = re.findall(pattern, string)

destinations = []
points = 0

for match in matches:
    destination = match[1]
    destinations.append(destination)

    points += len(destination)

print(f"Destinations: {(', ').join(destinations)}")
print(f"Travel Points: {points}")
