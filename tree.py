import os


def print_directory(file_path: str):
    file_list = []
    file_open = open('directory_list.txt', 'w')
    for (dirpath, dirnames, filenames) in os.walk(file_path):
        for file_name in filenames:
            file_list.append(os.path.join(f'{dirpath}', f'{file_name}\n'))
    for file in file_list:
        file_open.write(file)
    file_open.close()
    with open('directory_list.txt', 'r') as file_handler:
        for line in file_handler:
            print(line)


print_directory('/Users/joe/PycharmProjects/Python8Ex')
