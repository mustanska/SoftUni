def is_exist(current_list, element):
    if element in current_list:
        return True
    return False


shopping_list = input().split("!")

while True:
    line = input()

    if line == "Go Shopping!":
        break

    command_data = line.split()
    command = command_data[0]
    item = command_data[1]

    if command == "Urgent":
        if not is_exist(shopping_list, item):
            shopping_list.insert(0, item)

    elif command == "Unnecessary":
        if is_exist(shopping_list, item):
            shopping_list.remove(item)

    elif command == "Correct":
        new_item = command_data[2]
        if is_exist(shopping_list, item):
            index = shopping_list.index(item)
            shopping_list[index] = new_item

    elif command == "Rearrange":
        if is_exist(shopping_list, item):
            shopping_list.remove(item)
            shopping_list.append(item)

print(*shopping_list, sep=", ")
