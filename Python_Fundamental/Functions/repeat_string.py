def repeating_a_string(string, times_to_repeat):
    new_string = string * times_to_repeat
    return new_string


current_string = input()
repeat = int(input())

final_string = repeating_a_string(current_string, repeat)
print(final_string)