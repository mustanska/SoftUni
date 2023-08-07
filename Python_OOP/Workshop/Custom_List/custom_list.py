from typing import Any, List, Sequence


class CustomList:
    def __init__(self, *args: Any):
        self.__list: List[Any] = [*args]

    def __check_index(self, index):
        if not (0 <= index < len(self.__list) or (-len(self.__list) <= index < 0)):
            raise IndexError("The index is out of range!")

    def __find_indices_by_value(self, value):
        try:
            indices = [i for i in range(len(self.__list)) if self.__list[i] == value]
            return indices
        except IndexError:
            raise ValueError("The value does not exist in the list.")

    def __check_iterable_object(self, obj):
        try:
            [element for element in obj]
        except TypeError:
            raise ValueError("This object is not iterable!")

    def append(self, value: Any) -> List[Any]:
        self.__list.append(value)
        return self.__list

    def remove(self, index: int) -> Any:
        self.__check_index(index)
        return self.__list.pop(index)

    def get(self, index: int) -> Any:
        self.__check_index(index)
        return self.__list[index]

    def extend(self, iterable: Sequence[Any]) -> List[Any]:
        self.__check_iterable_object(iterable)
        self.__list.extend(iterable)
        return self.__list

    def insert(self, index: int, value: Any) -> List[Any]:
        self.__check_index(index)
        self.__list.insert(index, value)
        return self.__list

    def pop(self) -> Any:
        return self.__list.pop()

    def clear(self) -> None:
        self.__list = []

    def index(self, value: Any) -> int:
        return self.__find_indices_by_value(value)[0]

    def count(self, value: Any) -> int:
        return len(self.__find_indices_by_value(value))

    def reverse(self) -> List[Any]:
        return self.__list[::-1]

    def copy(self) -> List[Any]:
        return self.__list.copy()

    def __repr__(self):
        return f"[{', '.join([str(arg) for arg in self.__list])}]"

