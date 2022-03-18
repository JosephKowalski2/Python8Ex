import os


def print_directory(file_path: str):
    list_of_files = os.listdir(file_path)
    file_list = list()
    file_open = open('directory_list.txt', 'w')
    for file in list_of_files:
        full_directory_path = os.path.join(file_path, file)
        if os.path.isdir(full_directory_path):
            file_list += print_directory(full_directory_path)
        else:
            file_list.append(full_directory_path)
    for file in file_list:
        file_open.write(file)
    file_open.close()
    with open('directory_list.txt', 'r') as file_handler:
        for line in file_handler:
            print(f'{line}\n')


# print_directory('/Users/joe/PycharmProjects/Python8Ex')
os.listdir('/Users/joe/PycharmProjects')