def naughty_or_nice_list(santa_list, *args, **kwargs):

    def check_elements(given_element, given_type):
        if is_unique_element(given_element):
            index = find_name_index(given_element)
            finds_kid_place(santa_list[index][1], given_type)
            santa_list.pop(index)

    def is_unique_element(given_element):
        count = 0

        for element in santa_list:
            count += element.count(given_element)

        if count == 1:
            return True

        return False

    def find_name_index(given_element):
        for index in range(len(santa_list)):
            if given_element in santa_list[index]:
                return index

    def finds_kid_place(given_name, given_type):
        if given_type == "Naughty":
            naughty_kids.append(given_name)

        elif given_type == "Nice":
            nice_kids.append(given_name)

    nice_kids, naughty_kids, not_found = [], [], []

    for arg in args:
        counting_number, kid_type = arg.split("-")

        check_elements(int(counting_number), kid_type)

    for name, kid_type in kwargs.items():
        check_elements(name, kid_type)

    result = ""
    if nice_kids:
        result += f"Nice: {', '.join(nice_kids)}\n"
    if naughty_kids:
        result += f"Naughty: {', '.join(naughty_kids)}\n"
    if santa_list:
        result += f"Not found: {', '.join([info[1] for info in santa_list])}"

    return result


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
