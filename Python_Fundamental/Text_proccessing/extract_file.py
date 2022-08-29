file_path = input().split("\\")
# print(file_path)
searched_name_extension = file_path[-1]
# print(searched_name_extension)
searched_name_extension = searched_name_extension.split(".")
file_name = searched_name_extension[0]
file_extension = searched_name_extension[1]
print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
