def get_magic_triangle(n):
    magic_triangle = [[1], [1, 1]]

    for row in range(3, n + 1):
        magic_triangle_row = []

        for idx in range(row):
            if idx == 0:
                magic_triangle_row.append(magic_triangle[row - 2][idx])
            elif idx == row - 1:
                magic_triangle_row.append(magic_triangle[row - 2][idx - 1])
            else:
                magic_triangle_row.append(magic_triangle[row - 2][idx] + magic_triangle[row - 2][idx - 1])

        magic_triangle.append(magic_triangle_row)

    return magic_triangle


print(get_magic_triangle(5))
