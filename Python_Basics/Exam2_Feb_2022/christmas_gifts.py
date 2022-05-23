command = input()
number_adults = 0
number_kids = 0
number_toys = 0
number_shirts = 0


while command != "Christmas":
    age = int(command)
    if age <= 16:
        number_kids += 1
        number_toys += 1
    else:
        number_adults += 1
        number_shirts += 1
    command = input()

money_kids = number_toys * 5
money_adults = number_shirts * 15

print(f"Number of adults: {number_adults}")
print(f"Number of kids: {number_kids}")
print(f"Money for toys: {money_kids}")
print(f"Money for sweaters: {money_adults}")