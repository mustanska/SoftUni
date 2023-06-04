def numbers_searching(*numbers):
    duplicate_numbers = sorted({number for number in numbers if numbers.count(number) > 1})
    missing_number = 0

    for number in range(min(numbers), max(numbers) + 1):
        if number not in numbers:
            missing_number = number

    return [missing_number, duplicate_numbers]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
