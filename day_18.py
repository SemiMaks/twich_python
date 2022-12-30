# Библиотеки: пакеты и модули
import sys

# import sqlalchemy
# print(sqlalchemy)
# import sqlalchemy.schema
# from sqlalchemy import schema
# col = sqlalchemy.schema.Column()
# fk = sqlalchemy.schema.ForeignKey()

# print(dir(col))

# import sys
# path = sys.path
# for i in path:
#     print(i)

# import json
# import sys
# path = json.__file__
# path_s = dir(sys)
# print(path)
# print(path_s)

# Упражнение 25.7.1
# Создайте модуль begin.py, который содержит функцию с именем prime.
# Функция prime должна получать число и возвращать логический признак того,
# является ли число простым (то есть делится ли оно только на 1 и на себя).
# Перейдите в другой каталог, запустите Python и выполните команду
# from begin import prime
# Попытка должна завершиться неудачей. Обновите переменную sys.path, чтобы
# вы могли импортировать функцию из модуля. Затем присвойте значение PYTHONPATH.

#
# from begin import prime
# prime(6)

# Упражнение 25.7.2
# Создайте пакет utils. В файле __init__.py разместите код prime
# из предыдущего примера. Перейдите в другой каталог в терминале,
# запустите Python и выполните команду
# from utils import prime
# Попытка должна завершиться неудачей. Обновите переменную sys.path,
# чтобы вы могли импортировать функцию из пакета. Затем присвойте значение PYTHONPATH.

from utils import prime
# path = sys.path
# for p in path:
#     print(p)
    # PYTHONPATH = 'C:\WORKS\\twich_python\utils'
prime(6)
