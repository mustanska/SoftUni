rows, cols = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
sum_numbers = 0

for inner_matrix in matrix:
    sum_numbers += sum(inner_matrix)

print(sum_numbers)
print(matrix)