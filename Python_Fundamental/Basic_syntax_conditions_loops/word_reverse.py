word = input()

length = len(word)
for i in range(length, 0, -1):
    print(word[i-1], end='')


# string = "Bulgaria"
# print(string[:: -1])
