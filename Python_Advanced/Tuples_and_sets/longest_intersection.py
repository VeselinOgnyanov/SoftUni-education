def current_intersection_function(start_first_range, end_first_range, start_second_range, end_second_range):
    first_collection = set([int(x) for x in range(int(start_first_range), (int(end_first_range + 1)))])
    second_collection = set([int(x) for x in range(int(start_second_range), int(end_second_range + 1))])
    first_intersection = first_collection.intersection(second_collection)
    return first_intersection


longest_intersection = []
number = int(input())

for _ in range(number):
    current_line = tuple(input().split("-"))
    current_list = ",".join(current_line).split(",")
    current_intersection = current_intersection_function(int(current_list[0]),
                                                         int(current_list[1]),
                                                         int(current_list[2]),
                                                         int(current_list[3]))
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f"Longest intersection is {[x for x in longest_intersection]} with length {len(longest_intersection)}")

