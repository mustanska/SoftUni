def words_sorting(*words):
    words_dict = {}

    for word in words:
        words_dict[word] = sum(ord(character) for character in word)

    result = ""

    for word, value in sorted(words_dict.items(), key=lambda x: -x[1] if sum(words_dict.values()) % 2 != 0 else x[0]):
        result += f"{word} - {value}\n"

    return result


print(words_sorting('escape', 'charm', 'mythology'))
print(words_sorting('escape', 'charm', 'eye'))
print(words_sorting('cacophony', 'accolade'))
