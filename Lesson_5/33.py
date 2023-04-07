import os

os.system('cls')


def if_number_Fool(n):
    if n == 2: return 'Простое число'
    if n == 1 or n % 2 == 0: return 'Непростое число'
    for i in range(3, int((n ** 0.5) + 1), 2):
        if n % i == 0: return 'Непростое число'
    return 'Простое число'

print(if_number_Fool(int(input('введите число: '))))
