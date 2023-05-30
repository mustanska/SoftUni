even_numbers = [int(x) for x in input().split("@")]
position = 0
failed_houses = 0

while True:
    line = input()

    if line == "Love!":
        print(f"Cupid's last position was {position}.")
        break

    command, length = line.split()
    position += int(length)

    if position >= len(even_numbers):
        position = 0

    even_numbers[position] -= 2

    if even_numbers[position] == 0:
        print(f"Place {position} has Valentine's day.")
    elif even_numbers[position] < 0:
        even_numbers[position] = 0
        print(f"Place {position} already had Valentine's day.")


for num in even_numbers:
    if num != 0:
        failed_houses += 1

if failed_houses > 0:
    print(f"Cupid has failed {failed_houses} places.")
else:
    print("Mission was successful.")
