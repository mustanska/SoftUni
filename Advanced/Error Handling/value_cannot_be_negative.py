#The comment was added in the class because the condition

class ValueCannotBeNegative(Exception):
    """ValueCannotBeNegative"""
    pass


for _ in range(5):
    number = int(input())

    if number < 0:
        raise ValueCannotBeNegative

