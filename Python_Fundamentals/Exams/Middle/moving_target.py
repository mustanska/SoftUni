def is_exist(current_list, current_index):
    if current_index in range(len(current_list)):
        return True
    return False


targets = [int(x) for x in input().split()]

while True:
    line = input()

    if line == "End":
        print(*targets, sep="|")
        break

    command, index_str, value_str = line.split()
    index = int(index_str)
    value = int(value_str)

    if command == "Shoot":
        if is_exist(targets, index):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)

    elif command == "Add":
        if is_exist(targets, index):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif command == "Strike":
        if is_exist(targets, index) and is_exist(targets, index - value) and is_exist(targets, index + value):
            for _ in range(value * 2 + 1):
                targets.pop(index - value)
        else:
            print("Strike missed!")
