import re

text = input()

pattern = r"(::|\*\*)([A-Z][a-z]{2,})\1"
numbers = re.findall(r"\d", text)
emojis = re.findall(pattern, text)
limit_cool_threshold = 1
cool_emojis = []

for number in numbers:
    limit_cool_threshold *= int(number)

print(f"Cool threshold: {limit_cool_threshold}")

for emoji in emojis:
    cool_threshold = sum([ord(ch) for ch in emoji[1]])

    if cool_threshold >= limit_cool_threshold:
        cool_emoji = emoji[0] + emoji[1] + emoji[0]
        cool_emojis.append(cool_emoji)

print(f"{len(emojis)} emojis found in the text. The cool ones are:")
print(*cool_emojis, sep="\n")