"""
Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):

$ ls -l | python3 get_mean_size.py

Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l,
а возвращает средний размер файла в каталоге.
"""

import sys

lines = sys.stdin.readlines()[1:]
def get_mean_size(lines):

    average_size = 0
    count = 0

    if not lines:
        return 'No files'
    else:
        for line in lines:
            line = line.split()
            average_size += int(line[4])
            count += 1

    return round(average_size / count, 2)


if __name__ == '__main__':
    print(f'Average size of file is {get_mean_size(lines)} bytes.')


