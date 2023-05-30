def is_exist(index, text):
    return 0 <= index < len(text)


destinations = input()

while True:
    line = input()

    if line == "Travel":
        break

    line = line.split(":")
    command = line[0]

    if command == "Add Stop":
        idx = int(line[1])
        string = line[2]

        if is_exist(idx, destinations):
            destinations = destinations[0:idx] + string + destinations[idx:]

    elif command == "Remove Stop":
        start_idx = int(line[1])
        end_idx = int(line[2])

        if is_exist(start_idx, destinations) and is_exist(end_idx, destinations):
            destinations = destinations[0:start_idx] + destinations[end_idx + 1:]

    elif command == "Switch":
        old_str = line[1]
        new_str = line[2]

        if old_str in destinations:
            destinations = destinations.replace(old_str, new_str)

    print(destinations)

print(f"Ready for world tour! Planned stops: {destinations}")