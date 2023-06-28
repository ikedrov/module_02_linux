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
def get_summary_rss(ps_output_file_path: str) -> str:

    summ = 0
    kbytes = 2 ** 10
    kbytes_labels = {0: '', 1: 'kilo', 2: 'mega', 3: 'giga', 4: 'tera'}
    count = 0

    with open(ps_output_file_path, 'r') as f:
        f = f.readlines()[1:]
        for i in range(len(f)):
            lst = f[i].split()
            summ += int(lst[5])

    while summ > kbytes:
        summ /= kbytes
        count += 1

    return f'{str(round(summ, 2))} {kbytes_labels[count]}bytes'


if __name__ == '__main__':
    path: str = os.path.abspath('output_file.txt')
    summary_rss: str = get_summary_rss(path)
    print(summary_rss)

