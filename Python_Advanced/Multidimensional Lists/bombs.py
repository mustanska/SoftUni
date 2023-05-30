def find_alive_cells(matrix, size):
    cells = []
    for i in range(size):
        for j in range(size):
            if matrix[i][j] > 0:
                cells.append(matrix[i][j])

    return cells


def reduce_cells(matrix, cell_row, cell_col):
    current_element = matrix[cell_row][cell_col]
    matrix[cell_row][cell_col] = 0

    for x, y in coordinates:
        if cell_row + x < 0 or cell_row + x > n - 1 or cell_col + y < 0 or cell_col + y > n - 1:
            continue

        if matrix[cell_row + x][cell_col + y] > 0:
            matrix[cell_row + x][cell_col + y] -= current_element


n = int(input())

coordinates = (
    (-1, 0),
    (-1, - 1),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)

numbers = [[int(x) for x in input().split()] for _ in range(n)]
bombs_coordinates = [[int(el) for el in coordinates.split(",")]for coordinates in input().split()]

for bomb in bombs_coordinates:
    row_bomb = bomb[0]
    col_bomb = bomb[1]
    for row in range(n):
        for col in range(n):
            if row == row_bomb and col == col_bomb and numbers[row][col] in find_alive_cells(numbers, n):
                reduce_cells(numbers, row, col)

alive_cells = find_alive_cells(numbers, n)
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*numbers_row) for numbers_row in numbers]