
meters_to_be_converted = int(input())


def meters_to_kilometers(meters):
    kilometers = meters / 1000
    return kilometers


result = meters_to_kilometers(meters_to_be_converted)
print(f"{result:.2f}")

