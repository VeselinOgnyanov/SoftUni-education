import math
figure =  input()
if figure == "square":
    a = float(input())
    S = a * a
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    S = a * b
elif figure == "circle":
    r = float(input())
    S = math.pi * (r * r)
elif figure == "triangle":
    a = float(input())
    h = float(input())
    S = (a * h) / 2

S = round(S, 3)
print(S)




