rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]

square_matrices = 0

for i in range(rows - 1):
    for j in range(cols - 1):
        current_element = matrix[i][j]

        if current_element == matrix[i + 1][j] and \
                current_element == matrix[i][j + 1] and \
                current_element == matrix[i + 1][j + 1]:
            square_matrices += 1

print(square_matrices)
