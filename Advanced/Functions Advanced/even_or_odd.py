def even_odd(*args):
    command = args[-1]
    even = []
    odd = []

    [even.append(number) if number % 2 == 0 else odd.append(number) for number in args[:-1]]
    if command == "even":
        return even
    else:
        return odd


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))