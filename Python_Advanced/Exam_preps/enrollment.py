def gather_credits(credits_needed, *courses):
    credits_gathered = 0
    enrolled_courses_list = []
    credits_are_gathered = False

    for key, value in courses:
        if credits_gathered >= credits_needed:
            credits_are_gathered = True
            break
        else:
            if key not in enrolled_courses_list:
                enrolled_courses_list.append(key)
                credits_gathered += value

    enrolled_courses_list = sorted(enrolled_courses_list)

    if credits_gathered >= credits_needed:
        joined_courses = ", ".join(enrolled_courses_list)
        return f"Enrollment finished! Maximum credits: {credits_gathered}." + "\n" + f"Courses: {joined_courses}"
    return f"You need to enroll in more courses! You have to gather {abs(credits_gathered - credits_needed)} credits more."


print(gather_credits(80, ("Basics", 27),))

print(gather_credits(60, ("Basics", 27), ("Fundamentals", 27), ("Advanced", 30), ("Web", 30)))
