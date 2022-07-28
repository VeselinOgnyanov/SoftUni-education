# # command = input()
# # global_list = []
# # new_dict = {}
# # while command != "fundamentals" and command != "programming_basics":
# #     current_list = command.split(":")
# #     global_list.append(current_list)
# #     for current_list_value in global_list:
# #         for element in current_list_value:
# #             if "fundamentals" in element:
# #                 new_dict[element[0]] = element[1]
# #
# #     command = input()
# #
# # print(global_list)
#
inp = []
while True:
    comm = input().split(":")
    if len(comm) == 1:
        course = "".join(comm)
        course = course.replace("_", " ")
        break
    inp.append(comm)

students_dict = {}
for element in inp:
    for element_2 in element:
        if course == element_2:
            students_dict[element[0]] = element[1]
for key, values in students_dict.items():
    print(f"{key} - {values}")





# students_dict = {course[2].replace(" ", "_"): {} for course in inp}
# for course in inp:
#     students_dict[course[2].replace(" ", "_")][course[0]] = int(course[1])
#
# out = [f"{user} - {students_dict[comm[0]][user]}" for user in students_dict[comm[0]]]
# print(*out, sep="\n")

# new_dict = {}
# command = input()
# if len(command) == 1:
#     course = command
#
# inp = [[a,a,], [b,b], [c,c]]
# for element in inp:
#     for element_2 in element:
#         if course in element_2:
#             new_dict[element[0]] = element[1]
#
# print(new_dict)
#



