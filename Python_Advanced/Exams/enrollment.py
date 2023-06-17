def gather_credits(total_credits, *courses_with_credits):
    credits_taken = 0
    courses = []

    for course_name, course_credits in courses_with_credits:
        if credits_taken < total_credits and course_name not in courses:
            credits_taken += course_credits
            courses.append(course_name)

    result = ""

    if credits_taken >= total_credits:
        result += f"Enrollment finished! Maximum credits: {credits_taken}.\nCourses: {', '.join(sorted(courses))}"

    else:
        result += f"You need to enroll in more courses! You have to gather {total_credits - credits_taken} credits more."

    return result


print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
