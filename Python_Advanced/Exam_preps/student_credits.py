def students_credits(*args):
    total_credits_for_diploma = 0
    total_courses_dict = {}
    sep_str_list = []
    string_to_print = ""

    for current_str in args:
        sep_str_list.append(current_str.split("-"))

    for name, cred, max_test_pts, d_points in sep_str_list:
        evaluated_credits = int(cred) * (((int(d_points) / int(max_test_pts)) * 100) / 100)
        evaluated_credits = round(evaluated_credits, 2)
        total_credits_for_diploma += evaluated_credits
        total_courses_dict[name] = evaluated_credits

    if total_credits_for_diploma >= 240:
        string_to_print += f"Diyan gets a diploma with {total_credits_for_diploma:.1f} credits." + "\n"
    else:
        string_to_print += f"Diyan needs {abs(total_credits_for_diploma - 240):.1f} credits more for a diploma." + "\n"

    sorted_dict = dict(sorted(total_courses_dict.items(), key= lambda x: -x[1]))

    for course, course_credits in sorted_dict.items():
        string_to_print += f"{course} - {course_credits:.1f}" + "\n"

    return string_to_print


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