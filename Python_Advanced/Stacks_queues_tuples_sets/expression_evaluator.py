from collections import deque

given_string = deque(input().split())
result = []

for _ in range(len(given_string)):
    current_symbol = given_string.popleft()
    if current_symbol.isdigit():
        result.append()
    else:
        if current_symbol == "*":

        elif current_symbol == "+":
            pass
        elif current_symbol == "-":
            pass
        else:                                # case for "/"
            pass

