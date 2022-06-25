word_list = input().split()
even_word_list = [element for element in word_list if len(element) % 2 == 0]
for elements in range(len(even_word_list)):
    print(even_word_list[elements])

