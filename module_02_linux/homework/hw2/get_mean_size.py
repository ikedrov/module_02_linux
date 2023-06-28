"""
Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):

$ ls -l | python3 get_mean_size.py

Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l,
а возвращает средний размер файла в каталоге.
"""

import sys

def get_mean_size(data):

    average_size = 0
    count = 0

    if not data:
        return 0
    else:
        for line in data:
            line = line.split()
            average_size += int(line[4])
            count += 1

    return round(average_size / count, 2)


if __name__ == '__main__':
    data: str = sys.stdin.readlines()[1:]
    mean_size: float = get_mean_size(data)
    print(mean_size)

