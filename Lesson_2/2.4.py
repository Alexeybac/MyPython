import os
os.system('cls')

N = int(input('Введите N арбузов:  '))
max = 0
min = 1000000

for i in range (N):
    kg = int(input(f"{i+1}-й арбуз весит (кг)?: "))
    if kg > max:
        max = kg
    if kg < min:
        min = kg
print(f'Cамый маленький арбуз весит {min} кг,'
      f'а самый большой арбуз весит {max} кг!')