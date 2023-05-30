def even_odd_filter(**numbers):
    filtered_numbers = {}
    for key, values in numbers.items():
        if key == "even":
            filtered_numbers[key] = [x for x in values if x % 2 == 0]

        if key == "odd":
            filtered_numbers[key] = [x for x in values if x % 2 != 0]

    return dict(sorted(filtered_numbers.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
odd=[1, 2, 3, 4, 10, 5],
even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
odd=[2, 2, 30, 44, 10, 5],
))