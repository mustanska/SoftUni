import os
import re

root_path = os.path.dirname(os.path.abspath(__file__))
words_file_path = os.path.join(root_path, "Text Files", "words.txt")
text_file_path = os.path.join(root_path, "Text Files", "input.txt")
result_file_path = os.path.join(root_path, "Text Files", "output.txt")

word_count = {}

with open(words_file_path, "r") as words_file:
    words = words_file.read().lower().split()

with open(text_file_path, "r") as text_file:
    text = text_file.read().lower()

for word in words:
    pattern = r"[^a-z]" + re.escape(word) + r"[^a-z]"
    matches = re.findall(pattern, text)

    if matches:
        word_count[word] = len(matches)

result = ""
for key, value in sorted(word_count.items(), key=lambda x: -x[1]):
    result += f"{key} - {value}\n"

with open(result_file_path, "w") as result_file:
    result_file.write(result)