from typing import Any, List, Sequence, Dict


class CustomList:
    def __init__(self, *args: Any):
        self.list: List[Any] = list(args)

    @property
    def list(self):
        return self.__list

    @list.setter
    def list(self, args):
        for element in args:
            self.__check_element_to_add(element)

        self.__list = list(args)

    def __check_index(self, index):
        if not (0 <= index < self.size() or (-self.size() <= index < 0)):
            raise IndexError("Index is out of range!")

    def __find_indices_by_value(self, value):
        indices = [i for i in range(self.size()) if self.list[i] == value]

        if not indices:
            raise ValueError("The value does not exist in the list.")

        return indices

    @staticmethod
    def __check_iterable_object(obj):
        try:
            [element for element in obj]
        except TypeError:
            raise ValueError("This object is not iterable!")

    @staticmethod
    def __is_empty_value(value):
        if value == 0 or value:
            return False
        return True

    def __check_element_to_add(self, value):
        if self.__is_empty_value(value):
            raise ValueError("Element cannot be empty!")

    def __get_values_of_elements(self):
        return [el if isinstance(el, int) or isinstance(el, float) else len(el) for el in self.list]

    def append(self, value: Any) -> List[Any]:
        self.__check_element_to_add(value)
        self.list.append(value)
        return self.list

    def remove(self, index: int) -> Any:
        self.__check_index(index)
        return self.list.pop(index)

    def get(self, index: int) -> Any:
        self.__check_index(index)
        return self.list[index]

    def extend(self, iterable: Sequence[Any]) -> List[Any]:
        self.__check_iterable_object(iterable)
        self.list.extend(iterable)
        return self.list

    def insert(self, index: int, value: Any) -> List[Any]:
        self.__check_index(index)
        self.list.insert(index, value)
        return self.list

    def pop(self) -> Any:
        return self.list.pop()

    def clear(self) -> None:
        self.list = []

    def index(self, value: Any) -> int:
        return self.__find_indices_by_value(value)[0]

    def count(self, value: Any) -> int:
        return len(self.__find_indices_by_value(value))

    def reverse(self) -> List[Any]:
        return self.list[::-1]

    def copy(self) -> List[Any]:
        return self.list.copy()

    def size(self) -> int:
        return len(self.list)

    def add_first(self, value) -> None:
        self.list.insert(0, value)

    def dictionize(self) -> Dict[Any, Any]:
        """
        Returns the list as a dictionary
        with KEYS - elements (with hashable type) on an even positions,
        and VALUES - elements on an odd positions or ' '.
        The element as a key with an unhashable type and the next element as a value will not be included.
        """

        custom_list_dict = {}

        for i in range(0, self.size(), 2):
            try:
                custom_list_dict[self.list[i]] = self.list[i + 1] if i + 1 < self.size() else " "
            except TypeError:
                ...

        return custom_list_dict

    def move(self, amount: int) -> List[Any]:
        first_part = self.list[:amount]
        second_part = self.list[amount:]
        self.list = second_part + first_part

        return self.list

    def sum(self) -> int or float:
        return sum(self.__get_values_of_elements())

    def overbound(self) -> int:
        given_list = self.__get_values_of_elements()
        max_value = max(given_list)
        return given_list.index(max_value)

    def underbound(self) -> int:
        given_list = self.__get_values_of_elements()
        min_value = min(given_list)
        return given_list.index(min_value)

    def sort(self, reverse=False) -> List[Any]:
        """
        MODIFIES and RETURNS the given list sorted by element value if the value is a number,
        otherwise takes its length in ascending order.
        If the reverse parameter is True, the list will be MODIFIED and RETURNED in descending order.
        """

        sorted_list = []
        given_list = self.__get_values_of_elements()

        while given_list:
            min_value_index = given_list.index(min(given_list))
            sorted_list.append(self.list[min_value_index])
            given_list.pop(min_value_index)
            self.remove(min_value_index)

        self.list = sorted_list

        if reverse:
            self.list = self.reverse()

        return self.list

    def __repr__(self):
        return f"[{', '.join([str(arg) for arg in self.list])}]"
