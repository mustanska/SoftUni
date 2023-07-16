class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = list(dictionary.items())
        self.current_idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_idx >= len(self.dictionary) - 1:
            raise StopIteration

        self.current_idx += 1
        return self.dictionary[self.current_idx]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)