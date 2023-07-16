from typing import Sequence


class reverse_iter:
    def __init__(self, sequence: Sequence):
        self.sequence = sequence
        self.start_idx = len(self.sequence)
        self.end_idx = 0
        self.current_idx = self.start_idx

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_idx <= self.end_idx:
            raise StopIteration

        self.current_idx -= 1
        return self.sequence[self.current_idx]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
