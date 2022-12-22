# https://unicode.org/emoji/charts/emoji-list.html

import emoji

print(emoji.emojize('Python is :thumbs_up: '))

print('\U0001F44D')
print('\U0001F63B')

str_de = 'This is example'
byte = str_de.encode()
print(byte)
str_en = byte.decode()
print(str_en)

byte_data = b'\xf0\x9f\x8d\x95'
str_ = byte_data.decode('utf8')
print(str_)

import locale

print(locale.getpreferredencoding(False))

result_1 = 'x\u00b2'
result_2 = 'x\N{SUPERSCRIPT TWO}'
result_1b = result_1.encode('utf8')
print(result_1)
print(result_2)
print(result_1b)
# print(help(UNICODE))
result_1bb = result_1.encode('ascii', errors='ignore')
print(result_1bb)

# Упражнение 20.7.1
# https://www.charset.org/utf-8/13
# https://ru.wikipedia.org/wiki/ASCII
# https://home.unicode.org/

sym = '\u30c4'
sym_t = '\N{Katakana Letter Du}'
sym_g = ''

print(sym)
print(sym_t)

ascii_symbol = sym.encode('ascii', errors='ignore')
print(ascii_symbol)

# Упражнение 20.7.2
# https://ru.wikipedia.org/wiki/%D0%AE%D0%BD%D0%B8%D0%BA%D0%BE%D0%B4
# https://www.utf8-chartable.de/unicode-utf8-table.pl?names=2&amp;utf8=string-literal
def utf8_ascii(kod):
    new = kod[::-1]
    print(new)

utf8_ascii('\U000000A9')

# Упражнение 20.7.3
with open('name.txt', 'r') as fin:
    read = fin.read()
    reverse_read = read[::-1]
    print(read)
    print(reverse_read)

# Упражнение 20.7.4
# https://unicode-table.com/ru/sets/quotation-marks/

base_string = 'Python comes with "batteries included"'
ascii_string = base_string.encode('ascii')
print(ascii_string)
ascii_str = ascii_string.decode('ascii')
print(ascii_str)

def ascii_to_utf8(ascii_string):
    utf8_string = ascii_string.encode('utf8')
    utf_s = utf8_string.decode('utf8')
    # replace_base_string = utf_s.replace('"', '\U0000201C')
    # rep_base_string = rep_base_string.replace('"', '\U0000201D')
    # print(replace_base_string)
    # utf8_string = rep_base_string.encode('utf8')
    # print(utf8_string)
    # # print(rep_base_string)
ascii_to_utf8(ascii_string)

# Упражнение 20.7.5
data = [':)', ';)', ':P', ':|']
def old_emoji(data):
    for d in data:

