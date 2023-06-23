"""
С помощью команды ps можно посмотреть список запущенных процессов.
С флагами aux эта команда выведет информацию обо всех процессах, запущенных в системе.

Запустите эту команду и сохраните выданный результат в файл:

$ ps aux > output_file.txt

Столбец RSS показывает информацию о потребляемой памяти в байтах.

Напишите функцию get_summary_rss, которая на вход принимает путь до файла с результатом выполнения команды ps aux,
а возвращает суммарный объём потребляемой памяти в человекочитаемом формате.
Это означает, что ответ надо перевести в байты, килобайты, мегабайты и так далее.
"""


import os.path

path = os.path.abspath('output_file.txt')
def get_summary_rss(file: str) -> str:

    summ = 0
    with open(file, 'r') as f:
        f = f.readlines()[1:]
        for i in range(len(f)):
            lst = f[i].split()
            summ += int(lst[5])


    if summ <= 1024:
        print(f'Memory usage: {round(summ, 2)} B')
    elif 1024 < summ <= 1024 * 1024:
        print(f'Memory usage: {round(summ / 1024, 2)} KiB')
    else:
        print(f'Memory usage: {round(summ / (1024 * 1024), 2)} MiB')


if __name__ == '__main__':

    get_summary_rss(path)
