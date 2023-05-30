import re

text = input()

pattern = r"([#|])(?P<name>[A-Za-z\s]+)\1(?P<date>\d{2}\/\d{2}\/\d{2})\1(?P<calories>\d+)\1"
matches = re.finditer(pattern, text)

total_calories = 0
foods = []

for match in matches:
    food = match.groupdict()
    foods.append(food)

    total_calories += int(food["calories"])

print(f"You have food to last you for: {total_calories // 2000} days!")

for food in foods:
    print(f"Item: {food['name']}, Best before: {food['date']}, Nutrition: {food['calories']}")