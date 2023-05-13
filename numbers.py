numbers = sorted([int(x) for x in input().split()], reverse=True)

average_number = sum(numbers) / len(numbers)
result = []

for num in numbers:
    if num > average_number:
        if len(result) < 5:
            result.append(num)

if result:
    print(*result, sep=" ")
else:
    print("No")
