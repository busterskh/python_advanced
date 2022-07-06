"""
Напишите функцию, которая будет по output команды ls возвращать средний размер файла в папке.
$ ls -l ./
В качестве аргумента функции должен выступать путь до файла с output команды ls
"""
import os


def get_mean_size(ls_output_path: str) -> float:
    total_size = 0
    count_file = 0
    with open(ls_output_path, 'r') as file:
        for string in file:
            string = string.split()
            if len(string) > 5:
                total_size += int(string[4])
                count_file += 1
    result = total_size / count_file
    return result


if __name__ == "__main__":
    print(get_mean_size(os.path.abspath('output_ls.txt')))
