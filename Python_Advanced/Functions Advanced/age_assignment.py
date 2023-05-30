def age_assignment(*names, **ages):
    result = ""
    for letter, age in sorted(ages.items()):
        for name in names:
            if name.startswith(letter):
                result += f"{name} is {age} years old.\n"

    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))