def is_exist(current_list, element):
    if element in current_list:
        return True
    return False


items = input().split(", ")

while True:
    line = input()

    if line == "Craft!":
        print(*items, sep=", ")
        break

    command, input_item = line.split(" - ")

    if command == "Collect":
        if not is_exist(items, input_item):
            items.append(input_item)

    elif command == "Drop":
        if is_exist(items, input_item):
            items.remove(input_item)

    elif command == "Combine Items":
        old_item, new_item = input_item.split(":")

        if is_exist(items, old_item) and not is_exist(items, new_item):
            old_item_index = items.index(old_item)
            items.insert(old_item_index + 1, new_item)

    elif command == "Renew":
        if is_exist(items, input_item):
            items.remove(input_item)
            items.append(input_item)
