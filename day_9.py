# info = {'first': 'Pete', 'last': 'Best'}
# print(info)
# print(type(info))
# # info_new = dict([('first', 'John'),
# #                  ('last', 'Smith')])
# # print(info_new)
# # print(type(info_new))
#
# info['age'] = 20
# info['occupation'] = 'Drummer'
#
# print(info['last'])
# print('laster' in info)
#
# new_last = info.get('laster', 'такого ключа в словаре нет')
# print(new_last)

# import collections
# names = ['Ringo', 'Paul', 'John', 'Ringo']
# count = {}
# for name in names:
#     count.setdefault(name, 0)
#     count[name] += 1
#
# for name in names:
#     if name not in count:
#         count[name] = 1
#     else:
#         count[name] += 1

# count = collections.Counter(['Ringo', 'Paul', 'John', 'Ringo'])
#
# print(count)
# print(count['Paul'])

# band1_names = ['Ringo', 'Paul', 'John', 'Gorge']
# band2_names = ['Paul']
# names_to_bands = {}
# for name in band1_names:
#     names_to_bands.setdefault(name, []).append('Beatles')
#
# for name in band2_names:
#     names_to_bands.setdefault(name, []).append('Wings')

# for name in band1_names:
#     if name not in names_to_bands:
#         names_to_bands[name] = []
#     names_to_bands[name].append('Beatles')
#
# for name in band2_names:
#     if name not in names_to_bands:
#         names_to_bands[name] = []
#     names_to_bands[name].append('Wings')
#
#
# print(names_to_bands['Paul'])

# from collections import defaultdict
#
# names_to_bands = defaultdict(list)
# for name in band1_names:
#     names_to_bands[name].append('Beatles')
# for name in band2_names:
#     names_to_bands[name].append('Wings')
#
# print(names_to_bands)

# new_dict = {'Ringo': ['Beatles'], 'Paul': ['Beatles', 'Wings'], 'John': ['Beatles'], 'Gorge': ['Beatles']}
# print(new_dict)
# del new_dict['Ringo']
# print(new_dict)


# data = {'Adam': 2, 'Zeek':5, 'Fred': 3}
# for name in data:

# for key in data.keys():
#     print(key)

# for key, value in data.items():
#     print(key, value)

# print(list(data.items()))

# for name in sorted(data.keys(),reverse=True):
#     reverse = True
#     print(name)

# Упражнение 16.9.1
# Создайте словарь info, в котором хранится ваше имя, фамилия и возраст.

# info = dict([('firstname', 'John'),
#              ('lastname', 'Smith'),
#              ('age', 35)])
# print(info['firstname'])

# Упражнение 16.9.2
# Создайте пустой словарь phone с подробной информацией о вашем телефоне.
# Добавьте в словарь данные о размере экрана, объеме памяти, ОС, фирме-производителе и т. д.

# my_phone = {}
# my_phone['firm'] = 'Asus'
# my_phone['model'] = 'M1 pro'
# my_phone['memory'] = '128 Gb'
#
# for k, v in my_phone.items():
#     print(k, v)
# # print(my_phone)

# Упражнение 16.9.3
# Напишите абзац текста в строке, заключенной в тройные кавычки. Используйте метод .split
# для создания списка слов. Создайте словарь для хранения счетчика вхождений каждого слова в абзаце.

# text = '''
# Напишите абзац абзац текста в строке, заключенной в тройные кавычки. Используйте метод .split для создания списка слов. Создайте словарь для хранения счетчика вхождений каждого слова в абзаце.
# '''
# print(text)
# text = text.replace('\n', '')
# text = text.split(' ')
# print(text)
# my_text = {}
# for word in text:
#     my_text.setdefault(word, 0)
#     my_text[word] += 1
#
# print(my_text)

# Упражнение 16.9.4
# Посчитайте, сколько раз используется каждое слово в абзаце текста Ральфа Уолдо Эмерсона.
pass

# Упражнение 16.9.5
# Напишите код для вывода анаграмм (слов, состоящих из тех же букв в другом порядке) из абзаца текста.

# my_list_text = '''
# Напишите код для вывода анаграмм (слов, состоящих из тех же букв в другом порядке) из абзаца текста.
# '''
#
# my_list_text = my_list_text.replace('(', '')
# my_list_text = my_list_text.replace(')', '')
# my_list_text = my_list_text.replace('.', '')
# my_list_text = my_list_text.replace(',', '')
# my_list_text = my_list_text.split()
# print(my_list_text)
#
# reverser_text = my_list_text[::-1]
# print(reverser_text)
# for word in reverser_text:
#     word = word[::-1]
#     print(word)

# Упражнение 16.9.6
# Алгоритм PageRank использовался для создания поисковой системы Google. Алгоритм назначает
# каждой странице ранг, основанный на количестве входящих ссылок. Он получает одно
# входное значение: список страниц, ссылающихся на другие страницы. Каждой странице изначально
# назначается ранг 1. Выполняется несколько итераций алгоритма — обычно 10. Для каждой итерации:
# ••
# страница передает свой ранг, разделенный на количество исходящих ссылок, каждой
# странице, с которой она связана ссылкой;
# ••
# перенесенный ранг умножается на коэффициент затухания, обычно равный 0,85.
# Напишите код для выполнения 10 итераций этого алгоритма со списком кортежей входных
# и выходных ссылок:



links = [('a', 'b'), ('a', 'c'), ('b', 'c')]
"""PageRank algorithm with explicit number of iterations.

Returns
-------
ranking of nodes (pages) in the adjacency matrix

"""

import numpy as np

def pagerank(M, num_iterations: int = 100, d: float = 0.85):
    """PageRank: The trillion dollar algorithm.

    Parameters
    ----------
    M : numpy array
        adjacency matrix where M_i,j represents the link from 'j' to 'i', such that for all 'j'
        sum(i, M_i,j) = 1
    num_iterations : int, optional
        number of iterations, by default 100
    d : float, optional
        damping factor, by default 0.85

    Returns
    -------
    numpy array
        a vector of ranks such that v_i is the i-th rank from [0, 1],
        v sums to 1

    """
    N = M.shape[1]
    v = np.ones(N) / N
    M_hat = (d * M + (1 - d) / N)
    for i in range(num_iterations):
        v = M_hat @ v
    return v

# M = np.array([[0, 0, 0, 0, 1],
#               [0.5, 0, 0, 0, 0],
#               [0.5, 0, 0, 0, 0],
#               [0, 1, 0.5, 0, 0],
#               [0, 0, 0.5, 1, 0]])
M = np.array([[0, 0.5, 0.5],
              [0, 0, 1],
              [0, 0, 0]])
v = pagerank(M, 100, 0.85)

print(v)


# https://en.wikipedia.org/wiki/PageRank
# https://graphonline.ru/