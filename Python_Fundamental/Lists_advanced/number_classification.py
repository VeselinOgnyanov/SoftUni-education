number = input().split(", ")
positive_int_list = list(map(lambda x: int(x), number))

positive_list = [x for x in positive_int_list if x >= 0]
negative_list = [x for x in positive_int_list if x < 0]
even_list = [x for x in positive_int_list if x % 2 == 0]
odd_list = [x for x in positive_int_list if x % 2 == 1]
positive_list = ", ".join(map(lambda x: str(x), positive_list))
negative_list = ", ".join(map(lambda x: str(x), negative_list))
even_list = ", ".join(map(lambda x: str(x), even_list))
odd_list = ", ".join(map(lambda x: str(x), odd_list))
# print(positive_list)

print(f"Positive: {positive_list}")
print(f"Negative: {negative_list}")
print(f"Even: {even_list}")
print(f"Odd: {odd_list}")
