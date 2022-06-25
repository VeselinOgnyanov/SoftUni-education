def odd_and_even_sum(number):
    sum_even = 0
    sum_odd = 0
    new_list = list(number)
    for element in new_list:
        int_element = int(element)
        if int_element % 2 == 0:
            sum_even += int_element
        else:
            sum_odd += int_element
    print(f"Odd sum = {sum_odd}, Even sum = {sum_even}")


current_string = input()
odd_and_even_sum(current_string)
