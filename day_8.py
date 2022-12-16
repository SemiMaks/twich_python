# for letter in ['c', 'a', 't']:
#     print(letter)
# print(letter)

# animals = ['cat', 'dog', 'bird']
# for index in range(len(animals)):
#     print(index, animals[index])

numbers = [3, 5, 9, -1, 3, 1]
# result = 0
# for item in numbers:
#     if item < 0:
#         continue
#     result = result + item
# print(result)

# print('bird' in animals)
# print(animals.index('bird'))

# names = ['John', 'Paul', 'George', 'Ringo']
# print(names)
# for name in names:
#     if name not in ['John', 'Paul']:
#         names.remove(name)
# print(names)

# names = ['John', 'Paul', 'George', 'Ringo']
# print(names)
# names_to_remove = []
# for name in names:
#     if name not in ['John', 'Paul']:
#         names_to_remove.append(name)
# print(names_to_remove)
# for name in names_to_remove:
#     names.remove(name)
# print(names)

# names = ['John', 'Paul', 'George', 'Ringo']
# print(names)
# for name in names[:]:
#     if name not in ['John', 'Paul']:
#         names.remove(name)
# print(names)

# positive = False
# result = 0
# print(positive)
# for num in numbers:
#     if num < 0:
#         break
#     result = num + result
# else:
#     positive = True
# print(positive)
# print(result)

# n = 3
# while n > 0:
#     print(n)
#     n = n - 1

# n = 3
# while True:
#     print(n)
#     n = n - 1
#     if n==0:
#         break

# Упражнение 15.9.1
# 1. Создайте список с именами друзей и коллег. Вычислите среднюю длину имен в списке.
# friends = ['Глеб', 'Анотон', 'Семен', 'Сергей', 'Александр']
# result = 0
# for i in friends:
#     print(len(i))
#     result = len(i) + result
# print(result)
# print(len(friends))
# arange = result / len(friends)
# print('Средняя длина имени в списке друзей составляет -', arange)

# Упражнение 15.9.2
# 2.Создайте список с именами друзей и коллег. Проведите поиск имени John в списке в цикле for.
# Если имя не найдено, выведите соответствующее сообщение (подсказка: используйте else).
# friends = ['Глеб', 'Анотон', 'Семен', 'Сергей', 'Александр']
# name_search = 'Семен'
# for i in friends:
#     if name_search in friends:
#         print('В списке друзей есть ', name_search)
#         break
# else:
#     print('Такого друга нет')

# Упражнение 15.9.3
# 3.Создайте список кортежей из имени, фамилии и возраста ваших друзей и коллег.
# Если возраст неизвестен, занесите значение None. Вычислите средний возраст, пропустив все значения
# None. Выведите каждое имя, за которым следует строка Old (возраст выше среднего) или Young
# (возраст ниже среднего).
# names = []
# age_names = []
# age = 0
# n = 0
# age_ar = 35
# person_ev = ('Евгений', 'Иванов', 32)
# person_rus = ('Руслан', 'Петров', None)
# person_d = ('Дмитрий', 'Бодров', 45)
# person_a = ('Антон', 'Кузнецов', 55)
# names.append(person_ev)
# names.append(person_rus)
# names.append(person_d)
# names.append(person_a)
# print(names)
#
# for i in names:
#     if i[2] == None:
#         continue
#     else:
#         if i[2] > age_ar:
#             age_names.append(i[0])
#             age_names.append(i[1])
#         age = age + i[2]
#         n = n + 1
#     # print(age)
# arange = age / n
# print('Средний возраст без учета неизвестных -', arange)
# print('Возраст выше среднего:', age_names)