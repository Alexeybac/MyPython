
from random import randint

set1 = [randint(1, 10) for _ in range(int(input('1ое множество: ')))]
print(set1)
set2 = [randint(1, 10) for _ in range(int(input('2ое множество: ')))]
print(set2)

rezult = set(set1).intersection(set(set2))
print('Результат: ', end= '')
print(*rezult)