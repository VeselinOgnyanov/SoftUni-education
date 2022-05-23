number_of_strings = int(input())
is_pure = True
for strings in range(number_of_strings):
    new_string = input()
    if "," in new_string or "_" in new_string or "." in new_string:
        print(f"{new_string} is not pure!")
        continue
    print(f"{new_string} is pure.")