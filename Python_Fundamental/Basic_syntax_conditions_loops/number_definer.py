selected_number = float(input())


def positive_negative_number(number):
    if number == 0:
        return "zero"
    elif number < 0:
        if abs(number) < 1:
            return "small negative"
        elif abs(number) < 1000000:
            return "negative"
        else:
            return "large negative"
    elif number > 0:
        if number < 1:
            return "small positive"
        elif number < 1000000:
            return "positive"
        else:
            return "large positive"


print(positive_negative_number(selected_number))

