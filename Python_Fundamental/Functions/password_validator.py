def check_password(password):
    cond_length = True
    cond_letter_or_digits = True
    cond_at_least_2_digits = True
    counter_digits = 0
    length_of_pass = len(password)
    if (length_of_pass < 6) or (length_of_pass > 10):
        cond_length = False
        print("Password must be between 6 and 10 characters")
    for element in password:
        if not element.isalpha():
            if not element.isdigit():
                cond_letter_or_digits = False
                print("Password must consist only of letters and digits")
    for element in password:
        if element.isdigit():
            counter_digits += 1
    if counter_digits < 2:
        cond_at_least_2_digits = False
        print("Password must have at least 2 digits")
    if cond_length and cond_letter_or_digits and cond_at_least_2_digits:
        print('Password is valid')


user_password = input()
check_password(user_password)

