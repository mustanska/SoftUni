encrypted_msg = input()

while True:
    line = input()

    if line == "Decode":
        break

    line = line.split("|")
    command = line[0]

    if command == "Move":
        number_of_letters = int(line[1])
        encrypted_msg = encrypted_msg[number_of_letters:] + encrypted_msg[:number_of_letters]
    elif command == "Insert":
        index = int(line[1])
        value = line[2]
        encrypted_msg = encrypted_msg[:index] + value + encrypted_msg[index:]
    elif command == "ChangeAll":
        substring = line[1]
        replacement = line[2]
        encrypted_msg = encrypted_msg.replace(substring, replacement)

print(f"The decrypted message is: {encrypted_msg}")