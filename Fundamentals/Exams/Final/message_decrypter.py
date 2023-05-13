import re

n = int(input())
pattern = r"^([$%])([A-Z][a-z]{2,})\1: (\[\d+\]\|\[\d+\]\|\[\d+\]\|)$"
regex_pattern = re.compile(pattern)

for _ in range(n):
    msg = input()

    matches = regex_pattern.match(msg)

    if matches is None:
        print("Valid message not found!")
        continue

    result = regex_pattern.findall(msg)

    tag = result[0][1]
    numbers = re.findall(r"\d+", result[0][2])

    decrypted_word = "".join([chr(int(num)) for num in numbers])

    print(f"{tag}: {decrypted_word}")