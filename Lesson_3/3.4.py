import os
os.system('cls')

massiv = [(input(f'{i+1}-е число массива=> ')) 
        for i in range(int(input('Длина массива N: ')))]
print(massiv)

count = sum([1 for i in range(len(massiv)-1) if massiv[i] < massiv[i+1]])

# Второй вариант:
count = 0
for i in range(len(massiv)-1):
    if massiv[i+1] > massiv[i]: count +=1
print(f'{count} эл., больше предыдущих.')
