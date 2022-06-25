def perfect_number(number_to_check):
    sum_of_dividers = 0
    for num in range(1, number):
        if number % num == 0:
            sum_of_dividers += num
    if sum_of_dividers == number_to_check:
        print("We have a perfect number!" )
    else:
        print("It's not so perfect.")


number = int(input())
perfect_number(number)
