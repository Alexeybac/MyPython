import os

os.system('cls')

def step(x, n):
    if n == 0: return 1
    return step(x, n - 1) * x
print('Результат: ', step(int(input('Введите число: ')),int(input('Введите степень: '))))

