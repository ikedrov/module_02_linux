"""
Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):

$ ls -l | python3 get_mean_size.py

Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l,
а возвращает средний размер файла в каталоге.
"""



lines = 'ls.txt'
def get_mean_size(lines):

    average_size = 0
    count = 0

    with open(lines, 'r') as l:
        l = l.readlines()[1:]
        if not l:
            return 'No files'
        else:
            for line in l:
                line = line.split()
                average_size += int(line[4])
                count += 1

    return round(average_size / count, 2)


if __name__ == '__main__':
    print(f'Average size of file is {get_mean_size(lines)} bytes.')


