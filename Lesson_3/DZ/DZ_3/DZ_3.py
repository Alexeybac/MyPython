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
rez = sum([i[1] for char in text for i in dict.items() if char.upper() in i[0]])
print(f'Общая стоимость введенного слова {rez} балла(ов).')