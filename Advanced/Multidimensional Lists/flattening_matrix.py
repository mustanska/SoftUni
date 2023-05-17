rows = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
flatten_matrix = []

for inner_matrix in matrix:
    flatten_matrix.extend(inner_matrix)

print(flatten_matrix)