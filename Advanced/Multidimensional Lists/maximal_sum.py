rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

sub_matrix = []
max_sum = float("-inf")

for i in range(rows - 2):
    for j in range(cols - 2):
        first_row = matrix[i][j:j+3]
        second_row = matrix[i+1][j:j+3]
        third_row = matrix[i+2][j:j+3]

        sum_elements = sum(first_row) + sum(second_row) + sum(third_row)

        if sum_elements > max_sum:
            max_sum = sum_elements
            sub_matrix = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")
[print(*row) for row in sub_matrix]
