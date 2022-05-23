command = input()

sum_of_prime = 0
sum_of_non_prime = 0
non_prime = False
while command != "stop":
    non_prime = False
    command = int(command)
    if command < 0:
        print("Number is negative.")
        command = input()
        continue
    for num in range(2, command):
        if command % num == 0:
            non_prime = True
            break
    if non_prime:
        sum_of_non_prime += command
    else:
        sum_of_prime += command
    command = input()

print(f"Sum of all prime numbers is: {sum_of_prime}")
print(f"Sum of all non prime numbers is: {sum_of_non_prime}")
