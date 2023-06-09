# ------------------------------------------------

# Напишите программу для печати всех уникальных значений в словаре.
#
# Input:  [{"V": "S001"}, {"V": "S002"},
#          {"VI": "S001"}, {"VI": "S005"},
#          {"VII": " S005 "}, {" V ":" S009 "},
#          {" VIII ":" S007 "}]
#
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

import os
os.system('cls')

list_dict = [{"V": "S001","VI": "S002"}, {"V": "S002"},
             {"VI": "S001"}, {"VI": "S005"},
             {"VII": " S005 ","VI": "S005"}, {"V": " S009 ","VI": "S005","VII": "S005"},
             {"VIII": " S007 "}]
print(list_dict)

txt =list()
for i in list_dict:
    d = i.values()
    di = list(d)
    dix = di[0]
    dixt = dix.strip()
    txt.append(dixt)
txt = set(txt)
print(f'Результат = > {txt}')

# Вариант в одну строку:
print(f'Результат = > {set(list(i.values())[0].strip() for i in list_dict)}')