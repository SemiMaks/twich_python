# Импорт модулей

# print(help(json))
# print(dir(json))

# my_info = {'name':'Maksim', 'age':'41'}
# print(type(my_info))
# print(my_info)
# print(my_info.values())
#
# serialaized = json.dumps(my_info, indent=4)
# print(serialaized)
# deserialized = json.loads(serialaized)
# print(deserialized)

import glob
import os
import sys

print(sys.argv)


# for filename in os.listdir("../twich_python"):
#     print(filename)

def file_dir(dir_path):
    file_list = []
    py_count = 0
    txt_count = 0
    csv_count = 0
    for filename in os.listdir(dir_path):
        file_list.append(filename)
    for file in glob.glob('*.txt'):
        txt_count += 1
    for file in glob.glob('*.py'):
        py_count += 1
    for file in glob.glob('*.csv'):
        csv_count += 1
    file_list = '\n'.join(file_list)

    print(f'Количество файлов с расширением: \n.py - {py_count}\n.txt - {txt_count}\n.csv - {csv_count}')
    # print(file_list)


file_dir('../twich_python')
