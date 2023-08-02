def even_odd_filter(**kwargs):
    dict_to_print = {}
    for key, values in kwargs.items():
        if key == "odd":
            dict_to_print[key] = list(filter(lambda x: (x % 2 == 1), values))
        elif key == "even":
            dict_to_print[key] = list(filter(lambda x: (x % 2 == 0), values))
    sorted_dict = dict(sorted(dict_to_print.items(), key=lambda x: x[1], reverse=True))
    return sorted_dict


# Create a function called even_odd_filter() that can receive a different number of named arguments.
# The keys will be "even" and/or "odd", and the values will be a list of numbers.
# When the key is "odd", you should extract only the odd numbers from its list.
# When the key is "even", you should extract only the even numbers from its list.
# The function should return a dictionary sorted by the length of the lists in descending order.
# There will be no case of lists with the same length.

print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5], even=[3, 4, 5, 7, 10, 2, 5, 5, 2],))
print(even_odd_filter(odd=[2, 2, 30, 44, 10, 5],))