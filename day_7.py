names = list()
# other_names = ['Fred', 'Charles']
# print(type(names))
# print(type(other_names))
# print(other_names)

# print(list('Matt'))

# print(names)
# names.append('Matt')
# names.append('Fred')
# print(names)
# print(names[1])
#
# names.insert(0, 'George')
# print(names)
# names[1] = 'Henry'
# print(names)
# names.append('Paul')
# print(names)

# names.remove('Paul')
# print(names)
#
# del names[1]
# print(names)
#
# names.sort()
# print(names)

# old = [5, 3, 6, -2, 1]
# print(old)
# nums_sorted = sorted(old)
# print(nums_sorted)


# things = [2, 6, 'abc', 'Zebra', 1]
# print(id(things))
# print(things)
# things.sort(key=str)
# print(things)
# print(id(things))
#
# new_things = sorted(things, key=str)
# print('ID new_thinks: ',id(new_things))
# print(new_things)

# names = range(0, 11, 2)
# print(names)
# print(list(names))


# a = range(0, 5)
# print(list(a))
# b = range(5, 10)
# print(list(b))
# both = list(a) + list(b)
# print(len(both))

# row = ('George', 'Guitar')
# row2 = ('Paul', 'Bass')
# print(row, row2)

# empty = ()
# print(type(empty))

# one = tuple([1])
# one = (1,)
# one = 1,
# print(type(one))
# print(one)

# p = tuple(['Steph', 'Curry', 'Guard'])
# p = 'Steph', 'Curry', 'Guard'
# p = ('Steph', 'Curry', 'Guard')
# print(type(p))
# print(p)
# # p.append('Golden')
#
# digits = [0, 1, 1, 2, 3, 4, 5, 6, 7, 8]
# print(digits)
# print(type(digits))
#
# digits_set = set(digits)
# print(digits_set)
# print(type(digits_set))
#
# print(9 in digits_set)
#
# odd = {1, 3, 5, 7, 9}
# print(type(odd))
# print(odd)
# print(digits_set)
#
# even = digits_set - odd
# print(even)
# print('-'*10)
# prime = {2, 3, 5, 7, 8}
# print(prime)
# print(even)
# prime_even = prime & even
# print(prime_even)
#
# numbers = odd | even
# print(numbers)

# first_five = {0,1,2,3,4}
# print(first_five)
# two_to_six = {2,3,4,5,6}
# print(two_to_six)
# in_one = first_five ^ two_to_six
# print(in_one)

# Упражнение 14.10.1

# my_friends = ['Евгений', 'Глеб', 'Руслан']
# print(my_friends)
# print(id(my_friends))
# # my_friends = sorted(my_friends)
# my_friends.sort()
# print(id(my_friends))
# print(my_friends)

# Упражнение 14.10.2
#
# my_info = ('Иван', 'Иванов', 35)
# ev_info = ('Евгений', 'Петров', 35)
# rus_info = ('Руслан', 'Бодров', 35)
# gl_info = ('Глеб', 'Кузнецов', 35)
# people = []
# people.append(my_info)
# people.append(ev_info)
# people.append(rus_info)
# people.append(gl_info)
# print(people)
# people.sort()
# print(people)

# Упражнение 14.10.3

# my_friends = {'Евгений', 'Глеб', 'Руслан'}
# people = {'Глеб', 'Анотон', 'Семен', 'Сергей', 'Александр'}
# resume = my_friends & people
# print(resume)

# Упражнение 14.10.4

# text = '''Посетите сайт проекта «Гутенберг»1 и найдите страницу текста из Шекспира. Вставьте текст в строку, заключенную в тройные кавычки. Создайте другую строку с абзацем текста из Ральфа Уолдо Эмерсона. Используйте метод .split строк для получения списка слов из каждого текста. При помощи операций с множествами найдите общие слова, встречающиеся в текстах обоих авторов, а также слова, уникальные для каждого автора.'''
# new_text = ('проекта «Гутенберг»1 в том числе')
# text = text.split(' ')
# text = set(text)
# print(text)
# new_text = new_text.split(' ')
# new_text = set(new_text)
# print(new_text)
# match = text & new_text
# print('Совпали: ', match)
# not_match = text ^ new_text
# print('Не совпали:', not_match)

# Упражнение 14.10.5

# my_friends = ['Евгений', 'Глеб', 'Руслан']
# people = ('Глеб', 'Анотон', 'Семен', 'Сергей', 'Александр')
# my_friends = set(my_friends)
# people = set(people)
# resume = my_friends - people
# print(resume)
