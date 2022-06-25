def smallest_of_ints(first, second, third):
    my_list = [first, second, third]
    return min(my_list)


first_int = int(input())
second_int = int(input())
third_int = int(input())

print(smallest_of_ints(first_int, second_int, third_int))