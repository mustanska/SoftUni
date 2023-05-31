import os
from string import punctuation

root_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_path, "Text Files", "text.txt")
result_file_path = os.path.join(root_path, "Text Files", "output.txt")

with open(file_path, "r") as file:
    rows = file.readlines()

with open(result_file_path, "w") as result:
    for i in range(len(rows)):
        current_row = rows[i]
        letters = 0
        punctuation_marks = 0

        for character in current_row:
            if character.isalpha():
                letters += 1
            elif character in punctuation:
                punctuation_marks += 1

        result.write(f"Line {i + 1}: {current_row[:-1]} ({letters})({punctuation_marks})\n")