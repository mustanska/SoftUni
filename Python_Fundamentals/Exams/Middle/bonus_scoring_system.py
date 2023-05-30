from math import ceil

number_of_students = int(input())
lectures = int(input())
add_bonus = int(input())
total_bonus = 0
max_attendance = 0

for _ in range(number_of_students):
    attendance = int(input())

    max_attendance = max(attendance, max_attendance)
if lectures > 0:
    total_bonus = max_attendance / lectures * (5 + add_bonus)

print(f"Max Bonus: {ceil(total_bonus)}.")
print(f"The student has attended {max_attendance} lectures.")
