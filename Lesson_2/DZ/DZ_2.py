from time import time
import os
os.system('cls')

sum = int(input('Сумма чисел равна: '))
proiz = int(input('Их произведение равно: '))
start = time()
N = abs(proiz)
if -4000000 <= N <= 4000000 :
    for y in range(-N, N):
        if (y*y - sum*y + proiz) == 0:
            x = sum - y
            print(y, x)
            break
        elif y == N-1:
            print('Вычислить не возможно!')
else:
    print('Извините, слишком большое произведение))), поменьше загадайте плз!')

print(time() - start)