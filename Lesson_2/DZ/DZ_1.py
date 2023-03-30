import os
os.system('cls')

n = int(input('Количество монеток: '))
i = 0
text = []
while i < n:
    x = (input(f'(1-Решка/0-Орел) {i+1}-я монетка => '))
    if x != '0' and x !='1' and x != ' ':
        print(f'!!!Не правильно!!! Введите => или 1-Решка, или 0-Орел!!!')      
    else:
        text.append(x)
        i += 1
print(text)
i = 0
count0 = count1 = 0
while i < len(text):
    if text[i] == '0':
        count0 +=1
    if text[i] == '1':
        count1 +=1
    i += 1
if count0 == count1:
    print(f'Количество Орлов({count0}) и Решек({count1}) совпадает.')
if count0 > count1:
    print(f'Решек(1) меньше, чем Орлов(0) = {count1}')
if count0 < count1:
    print(f'Орлов(0) меньше, чем Решек(1) = {count0}')