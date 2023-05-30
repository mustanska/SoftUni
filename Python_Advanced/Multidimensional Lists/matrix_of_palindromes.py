rows, cols = [int(x) for x in input().split()]

first_letter = ord("a")

for i in range(rows):
    for j in range(cols):
        print(f"{chr(first_letter)}{chr(first_letter + j)}{chr(first_letter)}", end=" ")

    print()
    first_letter += 1
