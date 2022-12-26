# Классы
#
# b = str("I'am string!")
# print(b)
# import random
# import time
#
#
# class CorrectChair:
#     ''' A Chair on a chairflit'''
#     max_ocupants = 4
#
#     def __init__(self, id):
#         self.id = id
#         self.count = 0
#
#     def load(self, number):
#         new_val = self._check(self.count + number)
#         self.count = new_val
#
#     def unload(self, number):
#         new_val = self._check(self.count - number)
#         self.count = new_val
#
#     def _check(self, number):
#         if number < 0 or number > self.max_ocupants:
#             raise ValueError('Ivalid count:{}'.format(number))
#         return number
#
#
# NUM_CHAIRS = 100
#
# chairs = []
# for num in range(1, NUM_CHAIRS + 1):
#     chairs.append((CorrectChair(num)))
#
#
# def avg(chairs):
#     total = 0
#     for c in chairs:
#         total += c.count
#     return total / len(chairs)
#
#
# in_use = []
# transported = 0
# while True:
#     # загрузка пассажиров
#     loading = chairs.pop(0)
#     in_use.append(loading)
#     in_use[-1].load(random.randint(0, CorrectChair.max_ocupants))
#
#     # выгрузка пассажиров
#     if len(in_use) > NUM_CHAIRS / 2:
#         unloading = in_use.pop(0)
#         transported += unloading.count
#         chairs.append(unloading)
#         print('Loading Chair{} Count:{} Avg:{:.2} Total:{}'.format(loading.id, loading.count, avg(in_use), transported))
#         time.sleep(.25)

# print(help(Chair))
# print(Chair)
# print(dir(Chair))
#
# print(Chair.max_ocupants)
# print(Chair.__class__)
# print(Chair.max_ocupants.__class__)
# print(Chair.load.__class__)

# chair = CorrectChair(27)
# # print(chair.id)
# # print(chair.count)
# print(chair.count)
# chair.load(3)
# # Chair.load(chair,2)
# print(chair.count)

# print(dir(chair))
# print(chair.__dict__)
#
# print(chair.__class__)

# Упражнение 21.9.1
# Представьте, что вы проектируете приложение для банка. Как должна выглядеть
# модель клиента? Какими атрибутами она должна обладать? Какие методы она должна поддерживать?

# class Client:
#     """ Client on bank"""
#     account =0
#     def __init__(self, id):
#         self.id = id
#         self.sum = 0
#
#     def add_money(self, sum):
#         new_sum = self._check(self.account + sum)
#         self.account = new_sum
#     def withdraw_money(self, sum):
#         new_sum = self._check(self.account - sum)
#         self.account = new_sum
#
#     def _check(self, account):
#         if account < 0:
#             print(f'На вашем счёте {account} средств!')
#         return account
#
# new_client = Client(1)
# # print(new_client.account)
#
# new_client. add_money(100)
# new_client.withdraw_money(150)
# # print(new_client.__dict__)

# Упражнение 21.9.2
# Представьте, что вы создаете игру из серии Super Mario. Нужно определить класс для представления
# героя игры Марио. Как он будет выглядеть? Если вы не знакомы с играми серии Super Mario,
# используйте свою любимую видео- или настольную игру для моделирования игрока.

# class Mario:
#     """ Персонаж игры Марио """
#     current_speed = 10
#
#     def __init__(self, name):
#         self.name = name
#
#     def run(self, speed):
#         self.current_speed += speed
#
#     def jump(self, high):
#         self.current_speed -= high
#
# person = Mario('Игрок9')
# print(person.__dict__)
# person.run(15)
# print(person.__dict__)
# person.jump(20)
# print(person.__dict__)

# Упражнение 21.9.3
# Создайте класс для моделирования твитов (сообщений в «Твиттере»). Если вы не знаете,
# что такое «Твиттер», в Википедии приводится следующее определение1: «[…] социальная сеть
# для публичного обмена сообщениями при помощи веб-интерфейса, SMS, средств мгновенного обмена
# сообщениями или сторонних программ-клиентов для пользователей интернета любого возраста».

# class Twitter:
#     """ Twitter социальная сеть """
#     twit = 0
#     twit_count = 0
#
#     def __init__(self, nickname):
#         self.nickname = nickname
#
#     def add_twit(self, note):
#         new_twit = self._check(self.twit + note)
#         self.twit = new_twit
#         self.twit_count += 1
#
#     def del_twit(self, note):
#         new_twit = self._check(self.twit - note)
#         self.twit = new_twit
#         self.twit_count -= 1
#
#     def _check(self, twit_count):
#         if twit_count < 1:
#             print('Опубликованных твитов нет')
#         return twit_count
#
# my_twit = Twitter('My_nick')
# # print(help(Twitter))
# my_twit.add_twit(1)
# # print(my_twit.__dict__)
# # my_twit.del_twit(1)
# print(my_twit.__dict__)

# Упражнение 21.9.4
# Создайте класс для моделирования бытового электроприбора (тостер, стиральная машина, холодильник и т. д.).
#
# class Toster:
#     """ My toster """
#
#     def __init__(self, title):
#         self.title = title
#
#     def materials(self, materials):
#         self.materials = materials
#
#     def mode(self, mode):
#         self.mode = mode
#
# toster = Toster('BUD')
# toster.materials('steel')
# toster.mode('heating')
# print(toster.__dict__)