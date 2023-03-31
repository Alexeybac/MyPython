import os
os.system('cls')

massiv = [int(input(f'{i+1}-е число массива: ')) 
    for i in range(int(input('Размер массива: ')))]
print(massiv)
x = int(input('Введите число Х: '))
r = [abs(x - i) for i in massiv]
min = r[0]
ind = 0
for i in range(len(r)):
    if r[i] < min:
        min = r[i] 
        ind = i
    
print(massiv[ind])