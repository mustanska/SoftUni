from collections import deque


def fill_the_box(height, length, width, *args):
    args = deque(args)
    size = height * length * width

    while args:
        element = args.popleft()

        if element == "Finish":
            return f"There is free space in the box. You could put {size} more cubes."

        size -= element

        if size < 0:
            args.appendleft(abs(size))
            return f"No more free space! You have {sum([x for x in args if isinstance(x, int)])} more cubes."



print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))