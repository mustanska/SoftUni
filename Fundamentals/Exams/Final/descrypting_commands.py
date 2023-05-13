string = input()

while True:
    line = input()

    if line == "Finish":
        break

    line = line.split()
    command = line[0]

    if command == "Replace":
        current_char = line[1]
        new_char = line[2]

        if current_char in string:
            string = string.replace(current_char, new_char)

        print(string)

    elif command == "Cut":
        start_idx = int(line[1])
        end_idx = int(line[2])

        if 0 <= start_idx < len(string) and 0 <= end_idx < len(string):
            string = string[:start_idx] + string[end_idx + 1:]
            print(string)
        else:
            print("Invalid indices!")

    elif command == "Make":
        up_low = line[1]

        if up_low == "Upper":
            string = string.upper()
        else:
            string = string.lower()

        print(string)

    elif command == "Check":
        check_str = line[1]

        if check_str in string:
            print(f"Message contains {check_str}")
        else:
            print(f"Message doesn't contain {check_str}")

    elif command == "Sum":
        start_idx = int(line[1])
        end_idx = int(line[2])

        if 0 <= start_idx < len(string) and 0 <= end_idx < len(string):
            substring = string[start_idx:end_idx + 1]
            sum_values = sum([ord(ch) for ch in substring])
            print(sum_values)
        else:
            print("Invalid indices!")
        