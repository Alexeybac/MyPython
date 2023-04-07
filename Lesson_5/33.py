import os

os.system('cls')


def if_number_Fool(n):
    if n == 2: return 'Простое число'
    if n == 1 or n % 2 == 0: return 'Непростое число'
    for i in range(3, int((n ** 0.5) + 1), 2):
        if n % i == 0: return 'Непростое число'
    return 'Простое число'


nums = list([i, if_number_Fool(i)] for i in range(int(input('введите число: '))))
for i in nums: print(f'{i[0]} -> {i[1]}')
