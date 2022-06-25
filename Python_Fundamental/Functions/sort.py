# def to_int(num):
#     return int(num)


sequence_of_numbers = input()
num_list = sequence_of_numbers.split(" ")
mapped_to_int_num_list = list(sorted(map(lambda x: int(x), num_list)))
# mapped_to_int_num_list = (mapped_to_int_num_list)
print(mapped_to_int_num_list)
