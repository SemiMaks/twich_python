# Субклассирование

class CorrectChair:
    ''' A Chair on a chairflit'''
    max_ocupants = 4

    def __init__(self, id):
        self.id = id
        self.count = 0

    def load(self, number):
        new_val = self._check(self.count + number)
        self.count = new_val

    def unload(self, number):
        new_val = self._check(self.count - number)
        self.count = new_val

    def _check(self, number):
        if number < 0 or number > self.max_ocupants:
            raise ValueError('Ivalid count:{}'.format(number))
        return number


class Chair6(CorrectChair):
    max_ocupants = 6


# sixer = Chair6(67)
#
# print(sixer.__dict__)
# print(Chair6.__bases__)
#
# sixer.load(6)
# print(sixer.__dict__)
#
# class StallChair(CorrectChair):
#     def __init__(self, id, is_stalled):
#         super().__init__(id)
#         self.is_stalled = is_stalled
#         self.stalls = 0
#
#     def load(self, number):
#         if self.is_stalled(number, self):
#             self.stalls += 1
#         super().load(number)
#
# import random
# def ten_percent(number, chair):
#     """ return True of time """
#     return random.random() < .1
#
# print(random.random() < .1)
# stall42 = StallChair(42, ten_percent)
# print(stall42.__dict__)

# Упражнение 22.4.1

# Создайте класс, представляющий кошку. Что может делать кошка?
# Какими свойствами она обладает? Создайте субкласс кошки, представляющий
# тигра. Как изменится поведение субкласса?
#
# class Cat:
#     """ Класс кошачьи """
#     danger = 0
#
#     def __init__(self, type):
#         self.type = type
#
#     def weight(self, weight):
#         self.weight = weight
#
#     def ability(self, ability):
#         self.ability = ability
#
#     def coat_color(self, color):
#         self.color = color
#
#     def display(self):
#         print(f'Тип: {self.type} \nвес: {self.weight} \nспособность: {self.ability} \nокрас: {self.color} \nстепень опасности: {self.danger}')
#
# cat = Cat('Мурка')
# cat.weight('5 кг')
# cat.ability('ловит мышей')
# cat.coat_color('дымчатая')
# # print(cat.__dict__)
# cat.display()
#
# class Tiger(Cat):
#     danger = 10
#
# tiger = Tiger('Шархан')
# tiger.weight('250 кг')
# tiger.ability('охотится на животных')
# tiger.coat_color('полосатый')
# tiger.display()

# Упражнение 22.4.2
# Создайте базовый класс, представляющий персонажа, после чего реализуйте четыре
# субкласса — для Марио, Луиджи, Тода и Принцессы.

class GameMario:
    speed = 0
    jump = 0
    power = 0
    special = '-'
    """ Класс Игрока для игры Марио"""

    def __init__(self, name):
        self.name = name

    def display(self):
        print(f'Тип: {self.name}, Скорость: {self.speed}, Прыжок: {self.jump}, Сила: {self.power}, Способность: {self.special}')


class Person(GameMario):
    def speed(self, speed):
        self.speed = speed

    def jump(self, jump):
        self.jump = jump

    def power(self, power):
        self.power = power

    def special(self, special):
        self.special = special

gamer = GameMario('Шаблон')
gamer.display()

mario = Person('Марио')
mario.speed(4)
mario.jump(4)
mario.power(4)
mario.special('-')
mario.display()
# print(mario.__dict__)

lui = Person('Луиджи')
lui.speed(3)
lui.jump(5)
lui.power(3)
lui.special('-')
lui.display()

tod = Person('Тод')
tod.speed(5)
tod.jump(2)
tod.power(5)
tod.special('-')
tod.display()

princes = Person('Принцесса')
princes.speed(2)
princes.jump(3)
princes.power(2)
princes.special('Парить')
princes.display()

