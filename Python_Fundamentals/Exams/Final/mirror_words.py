import re

text = input()

pattern = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"

matches = re.findall(pattern, text)

mirror_words = {}

for match in matches:
    first_word = match[1]
    second_word = match[2]
    if second_word == first_word[::-1]:
        mirror_words[first_word] = second_word

if matches:
    print(f"{len(matches)} word pairs found!")
else:
    print("No word pairs found!")

if mirror_words:
    print("The mirror words are:")
    print(", ".join([f"{first_word} <=> {second_word}" for first_word, second_word in mirror_words.items()]))
else:
    print("No mirror words!")
