def print_triangle(number):
    triangle = []

    for n in range(1, number * 2):
        if n <= number:
            triangle.append(n)
        else:
            triangle.pop()
        print(*triangle)


size = int(input())

print_triangle(size)
