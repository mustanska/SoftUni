even_numbers = set()
odd_numbers = set()

for row in range(1, int(input()) + 1):
    value_of_name = int(sum(ord(x) for x in input()) / row)

    even_numbers.add(value_of_name) if value_of_name % 2 == 0 else odd_numbers.add(value_of_name)

if sum(even_numbers) == sum(odd_numbers):
    print(*even_numbers.union(odd_numbers), sep=", ")
elif sum(odd_numbers) > sum(even_numbers):
    print(*odd_numbers.difference(even_numbers), sep=", ")
else:
    print(*even_numbers.symmetric_difference(odd_numbers), sep=", ")