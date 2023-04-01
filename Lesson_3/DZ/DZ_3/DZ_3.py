import os
os.system('cls')

dict = {"AEIOULNSTRАВЕИНОРСТ": 1,
        "DGДКЛМПУ": 2,
        "BCMPБГЁЬЯ": 3,
        "FHVWYЙЫ": 4,
        "KЖЗХЦЧ": 5,
        "JXШЭЮ": 8, 
        "QZФЩЪ": 10}

text = input('Введите слово:  ').upper()

rez = sum([dict[i] for char in text for i in list(dict.keys()) for j in i if char == j])

print(f'Общая стоимость введенного слова {rez} балла(ов).')