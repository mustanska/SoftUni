import os

characters = ("-", ",", ".", "!", "?")

root_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_path, "text.txt")

with open(file_path, "r") as file:
    rows = file.readlines()

for i in range(0, len(rows), 2):
    current_row = rows[i]
    for character in current_row:
        if character in characters:
            current_row = current_row.replace(character, "@")

    print(" ".join(current_row.split()[::-1]))
