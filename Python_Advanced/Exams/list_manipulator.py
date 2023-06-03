from collections import deque


def list_manipulator(list_of_numbers, command, definition, *numbers):
    list_of_numbers = deque(list_of_numbers)
    if command == "add":
        if definition == "beginning":
            list_of_numbers.extendleft(numbers[::-1])

        elif definition == "end":
            list_of_numbers.extend(numbers)

    elif command == "remove":
        if definition == "beginning":
            if numbers:
                for _ in range(numbers[0]):
                    list_of_numbers.popleft()
            else:
                list_of_numbers.popleft()

        elif definition == "end":
            if numbers:
                for _ in range(numbers[0]):
                    list_of_numbers.pop()
            else:
                list_of_numbers.pop()

    return list(list_of_numbers)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
