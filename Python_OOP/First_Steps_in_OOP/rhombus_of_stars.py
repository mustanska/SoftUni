def create_stars_row(n):
    print(" " * (size - n), end="")
    print("* " * n)


def create_upper_triangle():
    for row in range(1, size + 1):
        create_stars_row(row)


def create_bottom_triangle():
    for row in range(size - 1, 0, -1):
        create_stars_row(row)


def create_rhombus():
    create_upper_triangle()
    create_bottom_triangle()


size = int(input())

create_rhombus()
