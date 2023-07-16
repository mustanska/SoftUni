class vowels:
    def __init__(self, text: str):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "y", "u"]
        self.current_idx = -1

    @property
    def vowels_in_text(self):
        return [c for c in self.text if c.lower() in self.vowels]

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_idx >= len(self.vowels_in_text) - 1:
            raise StopIteration

        self.current_idx += 1
        return self.vowels_in_text[self.current_idx]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
