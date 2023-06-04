from collections import deque


def best_list_pureness(numbers, times_to_rotate):
    numbers = deque(numbers)

    pureness_value = 0
    count_rotations = 0

    for rotate in range(times_to_rotate + 1):
        value = sum([i * number for i, number in enumerate(numbers)])

        if value > pureness_value:
            pureness_value = value
            count_rotations = rotate

        numbers.appendleft(numbers.pop())

    return f"Best pureness {pureness_value} after {count_rotations} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)