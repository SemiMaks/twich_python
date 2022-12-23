# # Юникод
#
# import locale
# print(locale.getpreferredencoding(False))
#
# print('\U000000b2')
# result = 'x\u00b2'
# print(result)
# result_2 = 'x\N{SUPERSCRIPT TWO}'
# print(result_2)
# result_3 = 'x²'
# print(result_3)
# print(result == result_2 == result_3)
#
# print(result.encode('utf-8'))
# print(result.encode('ascii', errors='replace'))
# # print(help('unicode'))
#
# utf8_bytes = b'x\xc2\xb2'
# text = utf8_bytes.decode('cp949')
# print(text)
#
# with open('sq.utf8', 'w', encoding='cp949') as fout:
#     fout.write('x²')
# data = open('sq.utf8', encoding='cp949').read()
# print(data)

# Упражнение 20.7.1
# Посетите сайт http://unicode.org и загрузите таблицу с кодовыми пунктами.
# Выберите символ, не входящий в набор символов ASCII, и напишите код
# Python для вывода этого символа как по кодовому пункту, так и по имени.

# sym = '\u30c4'
# sym_t = '\N{Katakana Letter Du}'
# print(sym)
# print(sym_t)

# Упражнение 20.7.2
# Существуют различные символы Юникода, которые выглядят как перевернутые
# версии ASCII-символов. Найдите таблицу отображения этих символов (это будет
# несложно). Напишите функцию, которая получает строку ASCII-символов и
# возвращает перевернутую версию этой строки.

# def utf8_ascii(utf8_ascii):
#     new = utf8_ascii[::-1]
#     print(utf8_ascii)
#     print(new)
#
#
# utf8_ascii('x\N{SUPERSCRIPT TWO}')

# Упражнение 20.7.3
# Запишите в файл свое имя, записанное перевернутыми символами.
# Приведите примеры кодировок, которые поддерживали бы такую запись
# вашего имени. Приведите примеры кодировок, которые такую запись не
# поддерживают.
# name = ['\u041C', '\u0410', '\u043A', '\u0441', '\u0438', '\u043C']
# print(name)
# new_name = name[::-1]
# print(new_name)

# Упражнение 20.7.4
# Умные (или закругленные) кавычки не поддерживаются в ASCII.
# Напишите функцию, которая получает строку ASCII и возвращает строку,
# в которой двойные кавычки заменяются умными кавычками. Например, строка
# Python comes with ”batteries included” должна превратиться в Python
# comes with “batteries included” (если присмотреться повнимательнее,
# вы увидите, что открывающие кавычки закруглены не так, как закрывающие).

# b = '\U0000275E'
# a = '\U0000275D'
# base_string = 'Python comes with "batteries included"'
# print(base_string)
# new_b_s = "Python comes with \U0000275Dbatteries included\U0000275E"
# count = 0
# for i in range(0, 2):
#     index = base_string.find('"')
#     # print(index)
#     if count == 0:
#         temp = list(base_string)
#         temp[index] = a
#         base_string = "".join(temp)
#         count += 1
#     elif count == 1:
#         temp = list(base_string)
#         temp[index] = b
#         base_string = "".join(temp)
#         count += 1
# # print(new_b_s)
# print(base_string)

# Упражнение 20.7.5
# Напишите функцию, которая получает текст со смайликами в старом
# стиле (:), :P и т. д.) Используя таблицу эмодзи1, добавьте в свою
# функцию код для замены текстовых смайликов их Юникод-версиями из таблицы.
emoji = [':-)', ';-)', ':-P', ':-|']
new_emoji = ['\U0001F600', '\U0001F609', '\U0001F60B', '\U0001F610']
# print(emoji)
# print(new_emoji)


def old_to_new(old, new):
    for i in range(0, 4):
        emoji[i] = new_emoji[i]
        # print(emoji)
    print(emoji)


old_to_new(emoji, new_emoji)
