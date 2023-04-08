import os

os.system('cls')

def step(x, n):
    if n == 1: return x
    return step(x, n - 1) * x
print('Результат: ', step(int(input('Введите число: ')),int(input('Введите степень: '))))

