# Напишите программу, которая принимает
# на вход строку, и отслеживает, сколько
# раз каждый символ уже встречался.
# Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# a a a b c a a d c d d
# a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

txt = 'a a a b c a a d c d d'
import os
os.system('cls')

rez = txt.split()
print(rez)
# ========Вариант 1==========================
# for i in range(len(rez)):
#     count = 1
#     for j in range(i+1,len(rez)):
#         if rez[i] == rez[j]:
#             rez[j] += '_' + str(count)
#             count += 1
# print(rez)
# print(*rez)

# =========Вариант 2========================

dict = {}.fromkeys(rez, 0)
print(dict)
txt = []
for i in rez:
    txt.append(f'{i}_{dict[i]}'if dict[i] != 0 else i)
    dict[i] += 1
print(*txt)