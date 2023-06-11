from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

flowers = {
    "rose": "rose",
    "tulip": "tulip",
    "lotus": "lotus",
    "daffodil": "daffodil",
}

is_found_word = False

while vowels and consonants:
    letters = [vowels.popleft(), consonants.pop()]

    for flower in flowers:
        for letter in letters:
            flowers[flower] = flowers[flower].replace(letter, "")

        if not flowers[flower]:
            print(f"Word found: {flower}")
            is_found_word = True
            break

    if is_found_word:
        break

else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
