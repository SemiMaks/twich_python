# Исключения
import gc
import itertools

import rise

# def err():
#     1 / 0
#
#
# def start():
#     return middle()
#
#
# def middle():
#     return more()
#
#
# def more():
#     err()
# start()

# numerator = 10
# divisor = 0
# if divisor != 0:
#     result = numerator / divisor
# else:
#     result = None
# print(result)

# numerator = 10
# divisor = 2
# try:
#     if divisor == 0:
#         rise
#     result = numerator / divisor
#     print(result)
# except Exception as e:
#     print(e)
#
#
# finally:
#     print('Эта строка будет напечатана в любом случае')

# import timeit
# print(dir(timeit))
# default_number = 1
# def timeit(self, number=default_number):
#     """ Хронометраж """
#     it = itertools.repeat(None, number)
#     gcold = gc.isenabled()
#     gc.disable()
#     try:
#         timing = self.inner(it, self.timer)
#     finally:
#         if gcold:
#             gc.enable()
#         return timing
#
# timeit(10)


# import this
# print(this)

# def log(msg):
#     print(msg)
#     raise SyntaxError("Logging not up")
#
# def divide_work(x,y):
#     try:
#         res = x/y
#         print(res)
#     except ZeroDivisionError as ex:
#         log("System is down")
#         raise ArithmeticError() from ex
#
# divide_work(3,0)

# Упражнение 23.10.1
# Напишите программу, выполняющую функции простейшего калькулятора.
# Программа получает два числа, а затем запрашивает оператор. Обеспечьте корректную
# обработку ввода, который не преобразуется в числа. Обработайте ошибки деления на ноль.

# def number():
#     result = 0
#     try:
#         print('Введите первое число:')
#         num1 = int(input())
#         print('Введите второе число:')
#         num2 = int(input())
#     except ValueError:
#         print('Введено не число!')
#         exit()
#     print('Введите операнд (*,/, +,-):')
#     operand = input()
#
#     try:
#         if operand == '*':
#             result = num1 * num2
#         elif operand == '/':
#             result = num1 / num2
#         elif operand == '+':
#             result = num1 + num2
#         elif operand == '-':
#             result = num1 - num2
#         else:
#             print('неверный операнд!')
#         print(f'результат операции {num1} {operand} {num2} = ', result)
#     except ZeroDivisionError as ex:
#         print(ex)
#         result = None
# number()

# Упражнение 23.10.2
# Напишите программу, которая вставляет нумерацию перед строками файла.
# Имя файла передается программе в командной строке. Импортируйте модуль sys и
# прочитайте имя файла из списка sys.argv. Корректно обработайте возможность передачи несуществующего файла.

import sys

# print(sys.argv)


def add_num(filename):
    try:
        results = []
        with open('file23.txt', 'r', encoding='utf8') as fin:
            for line, lit in enumerate(fin):
                results.append('{0} - {1}'.format(line, lit))
            results = ''.join(results)
            print(results)
    except FileNotFoundError:
        print('Файл не найден')

add_num('file23.txt')
