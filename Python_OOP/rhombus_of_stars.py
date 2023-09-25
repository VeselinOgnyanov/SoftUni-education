rhombus_number = int(input())

for cur_time in range(rhombus_number + 1):
    print(((rhombus_number - cur_time) * " ") + (cur_time * "* "))

for cur_time in range(rhombus_number - 1, 0, -1):
    print(((rhombus_number - cur_time) * " ") + cur_time * "* ")
