text = input()

vowel_a = 1
vowel_e = 2
vowel_i = 3
vowel_o = 4
vowel_u = 5
sum_of_vowels = 0
for letter in text:
    if letter == "a":
        sum_of_vowels += 1
    elif letter == "e":
        sum_of_vowels += 2
    elif letter == "i":
        sum_of_vowels += 3
    elif letter == "o":
        sum_of_vowels += 4
    elif letter == "u":
        sum_of_vowels += 5
print(sum_of_vowels)

