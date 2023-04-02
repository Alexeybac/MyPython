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
rez = list([sum(x[1] for x in dict.items() for y in text if y in x[0])])
print(f'Общая стоимость введенного слова {rez} балла(ов).')