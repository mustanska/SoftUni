def func_executor(*funcs):
    result = ""
    for func, param in funcs:
        result += f"{func.__name__} - {func(*param)}\n"

    return result


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(
    func_executor(
        (sum_numbers, (1, 2)),
        (multiply_numbers, (2, 4))
    )
)


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result


def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(
    func_executor(
        (make_upper, ("Python", "softUni")),
        (make_lower, ("PyThOn",)),
    )
)