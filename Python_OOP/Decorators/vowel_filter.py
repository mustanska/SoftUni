def vowel_filter(function):
    vowel = ["a", "e", "i", "o", "u"]

    def wrapper():
        return [ch for ch in function() if ch in vowel]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
