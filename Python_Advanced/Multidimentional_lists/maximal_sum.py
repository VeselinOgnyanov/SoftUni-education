rows, cols = [int(x) for x in input().split()]

matrix = [list(map(int, input().split())) for i in range(rows)]

maximum_sum = float('-inf')
maximum_sum_sub_matrix = []
longest_list = []
first_row_list = []
second_row_list = []
third_row_list = []

for cur_row in range(rows - 2):
    for cur_col in range(cols - 2):

        current_sum = matrix[cur_row][cur_col] + matrix[cur_row][cur_col + 1] + matrix[cur_row][cur_col + 2] + \
                      matrix[cur_row + 1][cur_col] + matrix[cur_row + 1][cur_col + 1] + \
                      matrix[cur_row + 1][cur_col + 2] + matrix[cur_row + 2][cur_col] + \
                      matrix[cur_row + 2][cur_col + 1] + matrix[cur_row + 2][cur_col + 2]

        if current_sum > maximum_sum:
            maximum_sum = current_sum
            first_row_list = [matrix[cur_row][cur_col], matrix[cur_row][cur_col + 1], matrix[cur_row][cur_col + 2]]
            second_row_list = [matrix[cur_row + 1][cur_col], matrix[cur_row + 1][cur_col + 1],
                               matrix[cur_row + 1][cur_col + 2]]
            third_row_list = [matrix[cur_row + 2][cur_col], matrix[cur_row + 2][cur_col + 1],
                              matrix[cur_row + 2][cur_col + 2]]

longest_list.append(first_row_list)
longest_list.append(second_row_list)
longest_list.append(third_row_list)

print(f"Sum = {maximum_sum}")

for num in range(len(longest_list)):
    list_of_strings = map(str, longest_list[num])
    print(" ".join(list_of_strings))

