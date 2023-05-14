number_of_students = int(input())

students = {}

for _ in range(number_of_students):
    name, grade = tuple(input().split())
    grade = float(grade)

    if name not in students:
        students[name] = []

    students[name].append(grade)

for name, grades in students.items():
    avg_grade = sum(grades) / len(grades)
    print(f"{name} -> {' '.join([str('{:.2f}'.format(grade)) for grade in grades])} (avg: {avg_grade:.2f})")