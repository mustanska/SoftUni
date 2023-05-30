def check_index(current_list, index):
    if index in range(len(current_list)):
        return True
    return False


list_of_elements = input().split()
moves = 0

while list_of_elements:
    line = input()

    if line == "end":
        print("Sorry you lose :(")
        print(*list_of_elements, sep=" ")
        break

    first_index, second_index = [int(x) for x in line.split()]
    moves += 1

    if first_index == second_index \
            or not check_index(list_of_elements, first_index) \
            or not check_index(list_of_elements, second_index):
        middle_index = len(list_of_elements) // 2

        list_of_elements.insert(middle_index, f"-{moves}a")
        list_of_elements.insert(middle_index, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")

    else:
        if list_of_elements[first_index] == list_of_elements[second_index]:
            print(f"Congrats! You have found matching elements - {list_of_elements[first_index]}!")
            list_of_elements.pop(first_index)
            if first_index < second_index:
                list_of_elements.pop(second_index - 1)
            else:
                list_of_elements.pop(second_index)
        else:
            print("Try again!")
else:
    print(f"You have won in {moves} turns!")


