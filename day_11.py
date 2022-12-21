# my_pets = ['dog', 'cat', 'bird']
# new_pets = my_pets[:]
# print(id(my_pets))
# print(id(new_pets))
# print(new_pets)
# del my_pets[0]
# del my_pets[0]
# print(new_pets)
# print(my_pets[0:3:2])

# number = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# print(number[9:0:-1])
# print(number[::-1])
# # print(number[::4])

# print(list(range(0,7,3)))

# print(my_pets[2])
# print(my_pets[-1])
# print(my_pets[0:-1])
# print(my_pets[:2])
# print(my_pets[-3:])

# captains = ['Janeway', 'Picard', 'Sisko']
#
# for i in range(len(captains)):
#     print(len(captains))
#     print(captains[i])

# print(len(my_pets))
# print(my_pets[-1])
# my_corteg = ('Fred', 23, 'Senior')
# print(my_corteg[-1])

# Упражнение 18.5.1
# Создайте переменную с вашим именем, хранящимся в формате строки.
# Используйте операции индексирования для получения первого символа.
# Извлеките последний символ. Будет ли ваш код для извлечения
# последнего символа работать с именем произвольной длины?

# name = 'Максим'
# print(name[0])
# print(name[-1])

# Упражнение 18.5.2
# Создайте переменную filename. Предполагая, что за именем
# файла следует трехбуквенное расширение, найдите расширение с
# использованием операции среза. Так, для файла README.txt должно
# быть получено расширение txt. Будет ли ваш код работать с именами
# файлов произвольной длины?
# filename = 'file.txt'
# print(filename[-3:])

# Упражнение 18.5.3
# Создайте функцию is_palindrome для проверки того, что переданное слово
# одинаково читается в обоих направлениях.
def is_palindrome(leather):
    reverse_leather = leather[::-1]
    print(leather)
    print(reverse_leather)
    if reverse_leather == leather:
        print('Слово ', leather, 'является полиндромом')
    else:
        print('Слово ', leather, 'не полиндром')

is_palindrome('казак')
