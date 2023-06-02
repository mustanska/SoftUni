import os
from string import punctuation

root_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_path, "Text Files", "text.txt")

with open(file_path, "r") as file:
    rows = file.readlines()

with open("output.txt", "w") as result_file:
    for i in range(len(rows)):
        row = rows[i]
        letters = 0
        punctuation_marks = 0

        for character in row:
            if character.isalpha():
                letters += 1
            elif character in punctuation:
                punctuation_marks += 1

        result = f"Line {i + 1}: {row[:-1] if i < len(rows) - 1 else row} ({letters})({punctuation_marks})\n"
        result_file.write(result)
        