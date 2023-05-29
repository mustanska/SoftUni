import re


class NameTooShortError(Exception):
    pass


class NameContainInvalidCharacterError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class MustBeOnlyOneSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MustContainDomainError(Exception):
    pass


valid_domains = [".com", ".bg", ".org", ".net"]

email = input()

while email != "End":
    # Checks for the special symbol "@" in the given email
    if email.count("@") < 1:
        raise MustContainAtSymbolError("Email must contain @")
    elif email.count("@") > 1:
        raise MustBeOnlyOneSymbolError("Email must not contain more than one @")
    else:
        name, domain_part = email.split("@")

    # Checks for correct name length and invalid characters
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if not re.match(r"^\w+$", name):
        raise NameContainInvalidCharacterError("Name must have only letters, digits and _")

    # Checks for the valid domain
    domain = re.findall(r"\.[a-z]+", domain_part)

    if not domain:
        raise MustContainDomainError("The email must contain correct domain")

    if domain[0] not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    email = input()

