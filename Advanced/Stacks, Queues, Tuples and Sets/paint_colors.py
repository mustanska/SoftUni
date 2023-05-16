from collections import deque

substrings = deque(input().split())

colors = ["red", "blue", "green", "orange", "purple", "yellow"]

secondary_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"}
}

found_colors = []

while substrings:
    first_substring = substrings.popleft()
    second_substring = substrings.pop() if len(substrings) >= 1 else ""

    color = {first_substring + second_substring, second_substring + first_substring}.intersection(colors)

    if color:
        found_colors.append(color.pop())
    else:
        first_substring = first_substring[:-1]
        second_substring = second_substring[:-1]
        idx = len(substrings) // 2

        if first_substring:
            substrings.insert(idx, first_substring)
        if second_substring:
            substrings.insert(idx, second_substring)

for color in found_colors:
    if color in secondary_colors.keys() and not secondary_colors[color].issubset(found_colors):
        found_colors.remove(color)

print(found_colors)