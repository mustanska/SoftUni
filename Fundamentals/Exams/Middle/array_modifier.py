
int_array = [int(x) for x in input().split()]

while True:
    line = input()

    if line == "end":
        break

    command_data = line.split()
    command = command_data[0]

    if command == "swap":
        first_index = int(command_data[1])
        second_index = int(command_data[2])

        int_array[first_index], int_array[second_index] = int_array[second_index], int_array[first_index]

    elif command == "multiply":
        first_index = int(command_data[1])
        second_index = int(command_data[2])

        int_array[first_index] = int_array[first_index] * int_array[second_index]

    elif command == "decrease":
        int_array = [x - 1 for x in int_array]

print(*int_array, sep=", ")