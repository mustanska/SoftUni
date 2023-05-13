first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students = int(input())

hour = 0

while students > 0:
    all_persons = first_employee + second_employee + third_employee
    hour += 1

    if hour % 4 == 0:
        continue

    students -= all_persons
else:
    print(f"Time needed: {hour}h.")
