def recursive_power(number, power):
    if power == 1:
        return number

    power -= 1

    return number * recursive_power(number, power)


print(recursive_power(2, 10))
print(recursive_power(10, 100))