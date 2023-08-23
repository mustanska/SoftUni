class HashTable:
    MAX_SIZE = 4

    def __init__(self):
        self.__max_capacity = HashTable.MAX_SIZE
        self.__length = 0
        self.__keys = [None] * self.__max_capacity
        self.__values = [None] * self.__max_capacity

    def __calculate_index(self, key):
        index = sum(ord(c) for c in key) % self.__max_capacity
        return self.__check_index(index)

    def __check_index(self, index):
        while True:
            if len(self) == self.__max_capacity:
                self.__increase_capacity()

            if self.__keys[index % self.__max_capacity] is None:
                return index % self.__max_capacity

            index += 1

    def __increase_capacity(self):
        self.__keys += [None] * self.__max_capacity
        self.__values += [None] * self.__max_capacity
        self.__max_capacity *= 2


    def __setitem__(self, key, value):
        index = self.__calculate_index(key)
        self.__keys[index] = key
        self.__values[index] = value
        self.__length += 1

    def __len__(self):
        return self.__length

    def __str__(self):
        return "{" + \
            ", ".join([f"{key}: {value}" for key, value in zip(self.__keys, self.__values) if key is not None]) + \
            "}"
