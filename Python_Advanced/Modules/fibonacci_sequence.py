command = input()

sequence = []

while command != "Stop":
    command = command.split()
    number = int(command[-1])

    if command[0] == "Locate":
        if number in sequence:
            indices = [i for i in range(len(sequence)) if sequence[i] == number]
            print(f"The number - {number} is at index", end=" ")
            print(*indices, sep=", ")
        else:
            print(f"The number {number} is not in the sequence")

    else:
        sequence = [0, 1]
        for num in range(2, number):
            sequence.append(sequence[-1] + sequence[-2])
        print(*sequence)

    command = input()
