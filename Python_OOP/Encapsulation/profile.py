class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value: str):
        if not (5 <= len(value) <= 15):
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value: str):
        is_correct_length = len(value) >= 8
        is_upper_letter_contains = len([ch for ch in value if ch.isupper()]) > 0
        is_digit_contains = len([ch for ch in value if ch.isdigit()]) > 0

        if not all([is_correct_length, is_upper_letter_contains, is_digit_contains]):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'

