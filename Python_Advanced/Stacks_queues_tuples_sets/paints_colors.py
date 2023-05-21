from collections import deque


def popping(first_list):
    list_to_pop = deque(first_list)
    list_to_pop.popleft()
    list_to_pop.pop()
    return list_to_pop


def strip_and_move(first_el_to_strip, second_el_to_strip, main_color_list):
    stripped_first_substring = first_el_to_strip[0:-1]
    stripped_last_substring = second_el_to_strip[0:-1]
    main_color_list = popping(main_color_list)
    if len(stripped_first_substring) >= 1:
        main_color_list.insert((len(main_color_list) // 2), stripped_first_substring)
    if len(stripped_last_substring) >= 1:
        main_color_list.insert((len(main_color_list) // 2), stripped_last_substring)
    return main_color_list


colors_input = deque(input().split(" "))

MAIN_COLORS = ["red", "yellow", "blue"]
SECONDARY_COLORS = ["orange", "purple", "green"]
found_colors = deque()
final_colors = []

while colors_input:
    if len(colors_input) > 1:
        first_substring, last_substring = colors_input[0], colors_input[-1]
        summed_substring = first_substring + last_substring
        reversed_summed_substring = last_substring + first_substring
        if summed_substring in MAIN_COLORS:
            found_colors.append(summed_substring)
            colors_input = popping(colors_input)
        elif reversed_summed_substring in MAIN_COLORS:
            found_colors.append(reversed_summed_substring)
            colors_input = popping(colors_input)
        elif summed_substring in SECONDARY_COLORS:
            found_colors.append(summed_substring)
            colors_input = popping(colors_input)
        elif reversed_summed_substring in SECONDARY_COLORS:
            found_colors.append(reversed_summed_substring)
            colors_input = popping(colors_input)
        else:
            colors_input = strip_and_move(first_substring, last_substring, colors_input)
    else:
        if colors_input[0] in MAIN_COLORS:
            if colors_input[0] not in found_colors:
                found_colors.append(colors_input[0])
                colors_input.pop()
        elif colors_input[0] in SECONDARY_COLORS:
            if colors_input[0] == "orange" and "orange" not in found_colors:
                found_colors.append("orange")
            elif colors_input[0] == "purple" and "purple" not in found_colors:
                found_colors.append("purple")
            elif colors_input[0] == "green" and "green" not in found_colors:
                found_colors.append("green")
        else:
            colors_input.pop()

for index in range(len(found_colors)):
    if found_colors[index] == "orange":
        if "red" in found_colors and "yellow" in found_colors:
            final_colors.append(found_colors[index])
    elif found_colors[index] == "purple":
        if "red" in found_colors and "blue" in found_colors:
            final_colors.append(found_colors[index])
    elif found_colors[index] == "green":
        if "blue" in found_colors and "yellow" in found_colors:
            final_colors.append(found_colors[index])
    else:
        final_colors.append(found_colors[index])
print(final_colors)
