straight_string = input().split()
for _ in range(len(straight_string)):
    last_element = straight_string.pop()
    print(last_element, end=" ")