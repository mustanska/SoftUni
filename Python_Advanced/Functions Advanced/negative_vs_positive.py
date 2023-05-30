def find_largest_sum(positive, negative):
    if abs(positive) < abs(negative):
        return "The negatives are stronger than the positives"
    else:
        return "The positives are stronger than the negatives"


numbers = []
sum_negative = 0
sum_positive = 0

for number in input().split():
    number = int(number)

    numbers.append(number)
    if number < 0:
        sum_negative += number
    else:
        sum_positive += number

print(sum_negative)
print(sum_positive)
print(find_largest_sum(sum_positive, sum_negative))