import os
from time import time

os.system('cls')

first = int(input('Введите первое число прогрессии: '))
step = int(input(('Введите шаг прогрессии: ')))
N = int(input('Введите число элементов прогрессии: '))
start = time()
#=========================
def Gpr(a, n, d):
    return a + (n - 1) * d
rezult = []
for i in range(1, N+1): rezult.append(Gpr(first, i, step))
print(*rezult)
#=========================
print(*(list(first + i * step for i in range(N)))) # Вариант в строку.
#=========================
print(time() - start)