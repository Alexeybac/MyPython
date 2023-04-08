import os

os.system('cls')

n = int(input('Введите размер массива N: '))
listN = list(map(int,input(f'Введите {n} чисел массива N через пробел: ').split()))

m = int(input('Введите размер массива M: '))
listM = list(int(input(f'Введите {m} чисел массива M построчно, через Enter: ')) for i in range(m))
print(listN)
print(listM)

rezult = list(filter(lambda x, y: x != y, listN, listM))

print(rezult)