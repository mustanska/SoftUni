activation_key = input()

while True:
    line = input()

    if line == "Generate":
        break

    line = line.split(">>>")
    command = line[0]
    str_to_change = ""

    if command == "Contains":
        substring = line[1]

        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif command == "Flip":
        upper_lower_command = line[1]
        start_idx = int(line[2])
        end_idx = int(line[3])

        for i in range(len(activation_key)):
            if start_idx <= i < end_idx:
                if upper_lower_command == "Upper":
                    str_to_change += activation_key[i].upper()
                else:
                    str_to_change += activation_key[i].lower()

        activation_key = activation_key[:start_idx] + str_to_change + activation_key[end_idx:]

        print(activation_key)

    elif command == "Slice":
        start_idx = int(line[1])
        end_idx = int(line[2])

        activation_key = activation_key[:start_idx] + activation_key[end_idx:]

        print(activation_key)

print(f"Your activation key is: {activation_key}")
