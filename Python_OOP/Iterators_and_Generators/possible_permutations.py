from itertools import permutations


def possible_permutations(list_elements):
    for element in permutations(list_elements):
        yield list(element)


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]