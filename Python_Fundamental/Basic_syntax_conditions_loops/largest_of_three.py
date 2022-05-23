import sys

first_number = int(input())
second_number = int(input())
third_number = int(input())

current_number = 0
smallest = -sys.maxsize
if first_number > smallest:
    current_number = first_number
if second_number > current_number:
    current_number = second_number
if third_number > current_number:
    current_number = third_number

print(current_number)
