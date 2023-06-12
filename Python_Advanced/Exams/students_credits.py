def students_credits(*strings):
    total_credits = 0
    courses_credits = {}

    for string in strings:
        course_name, course_credits, max_test_points, student_points = string.split("-")

        credit = int(course_credits) * int(student_points) / int(max_test_points)

        total_credits += credit

        courses_credits[course_name] = credit

    results = ""

    if total_credits >= 240:
        results += f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        results += f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.\n"

    for name, credit in sorted(courses_credits.items(), key=lambda x: -x[1]):
        results += f"{name} - {credit:.1f}\n"

    return results


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)