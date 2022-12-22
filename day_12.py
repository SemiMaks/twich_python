# Операции ввода/вывода. Файлы.

# print(dir(open))
# a_file = open('a.txt', 'w')
# passwd_file = open('a.txt', 'r')
# print(passwd_file.readlines())
# passwd_file.close()

# new_fin = open('b.text', 'r')
# print(new_fin.readline())

# bfin = open('1.png', 'rb')
# print(bfin.read(28))
# bfin.close()

# fin = open('a.txt', 'r')
# for line in fin:
#     print(line)
# fin.close()

# fout = open('c.txt', 'w')
# fout.write('George')
# fout.close()

# import os
# print(os.linesep)

# with open('c.txt', 'w') as fout:
#     fout.write('Ringo\r\n')
#     print('Запись завершена')

# filename = 'qwerty'
# def add_numbers(filename):
#     results = []
#     with open(filename) as fin:
#         for num, line in enumerate(fin):
#             results.append(
#                 '{0} -- {1}'.format(num, line))
#         print(results)
#         print(type(results))
#         return results

# def add_numbers(filename):
#     with open(filename) as fin:
#         return add_nums_to_seq(fin)
#
#
# def add_nums_to_seq(seq):
#     results = []
#     for num, line in enumerate(seq):
#         results.append('{0} -- {1}'.format(num, line))
#     print(results)
#     return results
#
#
# add_numbers('filename.txt')

# https://code.tutsplus.com/ru/tutorials/how-to-read-and-write-csv-files-in-python--cms-29907
# https://all-python.ru/osnovy/csv.html

# Упражнение 19.9.1
# Напишите функцию для записи файлов данных, разделенных запятыми (CSV, Comma Separated Values).
# Функция должна получать в параметрах имя файла и список кортежей. Кортежи должны содержать имя,
# адрес и возраст. Файл должен создать строку
# заголовка, за которой следует строка для каждого кортежа. Если функции будет передан следующий
# список кортежей:
# [('George', '4312 Abbey Road', 22),
# ('John', '54 Love Ave', 21)]
# в файл должны быть записаны следующие данные:
# name,address,age
# George,4312 Abbey Road,22
# John,54 Love Ave,21

import csv


values = [('Gerge', '4312 Abbey Road', 22),('John', '54 Love Ave', 21),('Иван', 'Тверская 26', 33)]

sheet = ('names', 'address', 'age')

def write_csv(file):
    global values
    global sheet
    with open(file, 'wt') as fout:
        writer = csv.writer(fout, delimiter=',', lineterminator='\r')
        writer.writerow(sheet)
        writer.writerows(values)
    print('Файл успешно записан')

write_csv('name.csv')


# Упражнение 19.9.1
# Напишите функцию для чтения CSV-файлов. Она должна возвращать список словарей,
# интерпретируя первую строку как имена ключей, а каждую последующую строку как значения
# этих ключей. Для данных в приведенном примере будет возвращен следующий результат:
# [{'name': 'George', 'address': '4312 Abbey Road', 'age': 22},
# {'name': 'John', 'address': '54 Love Ave', 'age': 21}]

with open('name.csv', newline='') as fin:
    list_dict = []
    reader = csv.DictReader(fin)
    for row in reader:
        # print(row)
        list_dict.append(row)
print(list_dict)
