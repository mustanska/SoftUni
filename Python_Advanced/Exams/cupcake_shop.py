from collections import deque


def stock_availability(cupcakes, action, *args):
    cupcakes = deque(cupcakes)

    if action == "delivery":
        cupcakes.extend(args)

    elif action == "sell":
        if not args:
            cupcakes.popleft()

        elif isinstance(args[0], int):
            [cupcakes.popleft() for _ in range(args[0])]

        else:
            for ordered_flavour in args:
                number_of_repetitions = cupcakes.count(ordered_flavour)
                for _ in range(number_of_repetitions):
                    cupcakes.remove(ordered_flavour)

    return list(cupcakes)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
