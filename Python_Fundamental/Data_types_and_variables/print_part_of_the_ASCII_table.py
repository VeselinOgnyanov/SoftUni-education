start_chars = int(input())
stop_chars = int(input())

for index in range(start_chars, stop_chars + 1):
    print(chr(index), end=" ")
