def age_assignment(*args, **kwargs):
    final_dict = {}
    string_to_print = ""
    for key, value in kwargs.items():
        for element in args:
            if key == element[0]:
                final_dict[element] = value
    final_dict = dict(sorted(final_dict.items(), key=lambda x: x[0]))
    for name, age in final_dict.items():
        string_to_print += f"{name} is {age} years old." + "\n"
    return string_to_print


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))