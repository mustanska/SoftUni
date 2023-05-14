from time import time

start = time()
numbers = [int(x) for x in input().split()]
target_number = int(input())

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target_number and numbers[i] != numbers[j]:
            print(f"{numbers[i]} + {numbers[j]} = {target_number}")
            break

# pairs = {}
# unique_numbers = set()
#
# for number in numbers:
#     if number in unique_numbers:
#         unique_numbers.remove(number)
#         first_number = pairs[number]
#         del pairs[number]
#         print(f"{first_number} + {number} = {target_number}")
#     else:
#         second_number = target_number - number
#         unique_numbers.add(second_number)
#         pairs[second_number] = number

end = time()

print(f"Time needed: {end - start}")