numbers = tuple([float(x) for x in input().split()])

numbers_as_dict = {}

for number in numbers:
    if number not in numbers_as_dict:
        numbers_as_dict[number] = numbers.count(number)

for number, count in numbers_as_dict.items():
    print(f"{number} - {count} times")