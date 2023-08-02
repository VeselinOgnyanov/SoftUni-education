def neg_vs_pos(*int_numbers):
    positive_list = []
    negative_list = []
    for element in int_numbers:
        for el in element:
            if el > 0:
                positive_list.append(el)
            else:
                negative_list.append(el)
    positive_sum = sum(positive_list)
    negative_sum = sum(negative_list)
    print(negative_sum)
    print(positive_sum)
    if abs(positive_sum) > abs(negative_sum):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


input_numbers = list(map(int, input().split(" ")))
neg_vs_pos(input_numbers)
