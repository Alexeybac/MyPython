import os
os.system('cls')

massiv = [int(input(f'{i+1}-е число массива: ')) 
    for i in range(int(input('Размер массива: ')))]
print(massiv)
x = int(input('Введите число Х:  '))
print(f'Число {x} в массиве повторяется'
      f' целых {sum([1 for i in massiv if i == x])} раз.')
