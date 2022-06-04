number_of_chars = int(input())
total_sum = 0

for number in range(number_of_chars):
    current_char = input()
    current_ASCII_code = ord(current_char)
    total_sum += current_ASCII_code

print(f"The sum equals: {total_sum}")