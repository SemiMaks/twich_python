# name = 'Matt'
# print(name)
# print(name == 'Matt')
# print(name != 'John')
# print(6 > 7)

# import functools


# @functools.total_ordering
# class Abs(object):
#     def __init__(self, num):
#         self.num = abs(num)
#
#     def __eq__(self, other):
#         return self.num == abs(other)
#
#     def __lt__(self, other):
#         return self.num < abs(other)
#
# five = -5
# four = -4
# print(five > four)
# print(type(five))
# print(type(four))
# print(five)
# print(four)

# score = 91
# if score > 90 and score < 100:
#     print(score, ' меньше 100 и болше 90')
# else:
#     print(score, 'вне диапазона')
#
# if 90 < score < 100:
#     print(score, ' меньше 100 и болше 90')
# else:
#     print(score, 'вне диапазона')

name = 'Paul'
# beatle = False
# print(beatle)
# if (name == 'Gorge' or
#     name == 'Ringo' or
#     name == 'John' or
#     name == 'Paul'):
#     beatle = True
# else:
#     beatle = False
# print(beatle)

# beatles = {'Gorge', 'Ringo', 'John', 'Paul'}
# beatle = name in beatles
# print(beatle)
#
# last_name = 'unknown'
# if name == 'Paul' and not beatle:
#     last_name = 'Revere'
# print(last_name)

# debug = False
# if debug:
#     print('Debugging')
# else:
#     print('Not debugging')


score = 57
# if score >= 90:
#     grade = 'A'
# else:
#     grade = 'B'
# print(grade)

# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade = 'D'
# else:
#     grade = 'F'
# print(grade)

# year = 2021
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(year, '- год високосный')
# else:
#     print(year, ' - не является високосным')

number = 897

if number % 2 == 0:
    print('остаток =', number % 2)
    print(number, '- четное число')
else:
    print('остаток = ', number % 2)
    print(number, '- не чётное число')
