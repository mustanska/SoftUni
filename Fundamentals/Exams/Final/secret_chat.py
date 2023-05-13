secret_msg = input()

while True:
    line = input()

    if line == "Reveal":
        break

    line = line.split(":|:")
    instruction = line[0]

    if instruction == "InsertSpace":
        index = int(line[1])
        secret_msg = secret_msg[:index] + " " + secret_msg[index:]
        print(secret_msg)

    elif instruction == "Reverse":
        substring = line[1]

        if substring in secret_msg:
            start_idx = secret_msg.index(substring)
            end_idx = start_idx + len(substring)
            substring = substring[::-1]

            secret_msg = secret_msg[:start_idx] + secret_msg[end_idx:] + substring
            print(secret_msg)
        else:
            print("error")

    elif instruction == "ChangeAll":
        substring = line[1]
        replacement = line[2]
        secret_msg = secret_msg.replace(substring, replacement)

        print(secret_msg)

print(f"You have a new text message: {secret_msg}")