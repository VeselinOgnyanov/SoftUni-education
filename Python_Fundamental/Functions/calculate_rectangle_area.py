def calculating_rectangle_area(a, b):
    calculated_area = a * b
    return calculated_area


width = int(input())
height = int(input())
area = calculating_rectangle_area(width, height)
print(area)