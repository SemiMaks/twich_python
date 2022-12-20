# def add_2(num, new_num):
#     """
#     :param num:
#     :return: return 2 more than num
#     """
#     result = num + new_num + 7
#     return result
# print(add_2(2, 2))
# print(type(add_2))
# print(id(add_2(2)))
# print(help(add_2))

# x = 2 # Глобальная переменная
# def scope_demo():
#     y = 4 # Локальная переменная
#     print('Локальная: {}'.format(y))
#     print('Глобальная: {}'.format(x))
#     print('Built-in: {}'.format(dir))
# scope_demo()
# print(x)
# print(y)

# def dir():
#     print('DIR переназначен')
#
# dir()
# del dir
# print(dir())
# y = 5
# def foo():
#     x = 10
#     print(locals())
#
# foo()

# def add_two_nums(a, b):
#     return a + b
#
# print(add_two_nums(3, 4))
# print(add_two_nums(3.7, 4.6))
# print(add_two_nums('3', '4'))

# def add_n(num, n=3):
#     '''
#     :param num:
#     :param n: dafault to adding 3
#     :return:
#     '''
#     return num + n
#
#
# print(add_n(5, 5))
# print(add_n(5))

# def to_list(value, default=None):
#     default = default if default is not None else []
#     default.append(value)
#     return default
#
# print(to_list(5))
# print(to_list(7))
# print(to_list('string'))
# print(to_list(-7))

# Упражнение 17.7.1
# Напишите функцию is_odd, которая получает целое число и возвращает True для
# нечетных чисел или False для четных.
# def is_odd(num):
#     if num % 2 == 0:
#         return False
#     else:
#         return True
#
# print(is_odd(5))

# Упражнение 17.7.2
# Напишите функцию is_prime, которая получает целое число и возвращает True
# для простых чисел или False для чисел, не являющихся простыми.
# https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D1%81%D1%82%D0%BE%D0%B5_%D1%87%D0%B8%D1%81%D0%BB%D0%BE
# def is_prime(num):
#     d = 2
#     while num % d != 0:
#         d += 1
#     return  d == num
#
# print(is_prime(7))

# Упражнение 17.7.3
# Напишите функцию бинарного поиска. Функция должна получать отсортированную
# последовательность и искомый элемент и возвращать индекс найденного элемента.
# Если элемент не найден, функция должна возвращать –1.
# https://ru.wikipedia.org/wiki/%D0%94%D0%B2%D0%BE%D0%B8%D1%87%D0%BD%D1%8B%D0%B9_%D0%BF%D0%BE%D0%B8%D1%81%D0%BA
# data = [3, 5, 8, 4, 2, 9, 1, 25, 43]
# data = sorted(data)
# # print(len(data))
#
#
# print(data)
# def binary(data, element):
#     low = 0
#     high = len(data) - 1
#     while low <= high:
#         middle = (low + high) // 2
#         if data[middle] == element:
#             return middle
#         elif data[middle] > element:
#             high = middle - 1
#         else:
#             low = middle + 1
#     return -1
#
#
# print(binary(data, 97))

# Упражнение 17.7.4
# Напишите функцию, которая получает строки в «верблюжьем регистре»
# (ThisIsCamelCased) и преобразует их в «змеиный регистр» (this_is_camel_cased).
# Измените функцию, добавив в нее аргумент separator, чтобы функция также могла
# выполнять преобразование к «кебаб-регистру» (this-is-camel-case).

text = '''ThisIsCamelCased'''
print(text)
separator = '_'

def change_case(text):
    new_text = ''
    for i in text:
        if (i.isupper()):
            new_text += separator + i.lower()
        else:
            new_text += i
    return new_text[1:]


print(change_case(text))
