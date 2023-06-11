from collections import deque


def check_seat(char, f_num, s_num):
    seat = ""
    first_passenger = f"{f_num}{char}"
    second_passenger = f"{s_num}{char}"

    if first_passenger in seats:
        seat = first_passenger

    if second_passenger in seats:
        seat = second_passenger

    return seat


seats = input().split(", ")

first_sequence = deque([int(x) for x in input().split(", ")])
second_sequence = deque([int(x) for x in input().split(", ")])

seats_taken = []
rotations = 0

while len(seats_taken) < 3 and rotations < 10:
    first_number = first_sequence.popleft()
    second_number = second_sequence.pop()

    rotations += 1

    character = chr(first_number + second_number)

    result = check_seat(character, first_number, second_number)

    if result:
        if result not in seats_taken:
            seats_taken.append(result)
    else:
        first_sequence.append(first_number)
        second_sequence.appendleft(second_number)

print(f"Seat matches: {', '.join(seats_taken)}")
print(f"Rotations count: {rotations}")