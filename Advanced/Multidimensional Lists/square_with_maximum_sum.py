from sys import maxsize

rows, cols = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]


max_sum = -maxsize
submatrix = []

for i in range(rows - 1):
    for j in range(cols - 1):
        current_element = matrix[i][j]
        bottom_element = matrix[i + 1][j]
        right_element = matrix[i][j + 1]
        diagonal_element = matrix[i + 1][j + 1]

        sum_elements = current_element + bottom_element + right_element + diagonal_element

        if sum_elements > max_sum:
            max_sum = sum_elements
            submatrix = [[current_element, right_element], [bottom_element, diagonal_element]]

for inner_matrix in submatrix:
    print(*inner_matrix)
print(max_sum)