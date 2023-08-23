from typing import Any


class HashTable:
    MAX_SIZE: int = 4

    def __init__(self):
        self.__max_capacity: int = HashTable.MAX_SIZE
        self.__length: int = 0
        self.__keys: list = [None] * self.__max_capacity
        self.__values: list = [None] * self.__max_capacity

    @staticmethod
    def __check_key(key: str):
        if not isinstance(key, str):
            raise ValueError("The key is not a string!")

    def __calculate_index(self, key: str) -> int:
        self.__check_key(key)
        index = sum(ord(c.upper()) if c.islower() else ord(c.lower()) for c in key) % self.__max_capacity
        return self.__check_index(index)

    def __check_index(self, index: int) -> int:
        while True:
            if len(self) == self.__max_capacity:
                self.__increase_capacity()

            if self.__keys[index % self.__max_capacity] is None:
                return index % self.__max_capacity

            index += 1

    def __increase_capacity(self) -> None:
        self.__keys += [None] * self.__max_capacity
        self.__values += [None] * self.__max_capacity
        self.__max_capacity *= 2

    def hash(self, key: str) -> int:
        return self.__calculate_index(key)
    def add(self, key: str, value: Any) -> None:
        self[key] = value

    def get(self, key: str, message: str = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return message

    def keys(self) -> list:
        return [key for key in self.__keys if key is not None]

    def values(self) -> list:
        return [value for value in self.__values if value is not None]

    def items(self) -> list:
        keys = self.keys()
        values = self.values()
        return list(zip(keys, values))
    def __getitem__(self, key: str):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            raise KeyError(f"The key is not in the hash table!")

    def __setitem__(self, key: str, value: Any):
        index = self.hash(key)
        self.__keys[index] = key
        self.__values[index] = value
        self.__length += 1

    def __delitem__(self, key: str):
        try:
            index = self.__keys.index(key)
            self.__keys[index] = None
            self.__values[index] = None
        except ValueError:
            raise KeyError(f"The key is not in the hash table!")


    def __len__(self):
        return self.__length

    def __str__(self):
        return "{" + \
            ", ".join([f"{key}: {value}" for key, value in zip(self.__keys, self.__values) if key is not None]) + \
            "}"
