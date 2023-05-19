def is_valid_index(idx, size):
    return 0 <= idx < size


rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]

while True:
    line = input()

    if line == "END":
        break

    command, *indices = [int(x) if x.isdigit() else x for x in line.split()]

    if command == "swap" and len(indices) == 4 \
            and is_valid_index(indices[0], rows) \
            and is_valid_index(indices[1], cols) \
            and is_valid_index(indices[2], rows) \
            and is_valid_index(indices[3], cols):
        matrix[indices[0]][indices[1]], matrix[indices[2]][indices[3]] = matrix[indices[2]][indices[3]], matrix[indices[0]][indices[1]]

        [print(*row, end="\n") for row in matrix]
    else:
        print("Invalid input!")