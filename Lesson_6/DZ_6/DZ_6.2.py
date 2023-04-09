from random import randint

n = list(randint(-10, 30) for _ in range(int(input('Введите размер множества: '))))
print(*n)
rang = list(int(input('Введите границы (от, до) диапазона:')) for _ in range(2))
print(f' От {rang[0]}  до {rang[1]}')
rezult = list(i for i in range(len(n)) if rang[0] < n[i] < rang[1])
print('Результат: =>', *rezult)
