a = int(input('Введем число А:  '))

f1 = 0
f2 = 1
count = 2

while a >= f2:
    if a == f2:
        print(f'Порядковый номер числа А в ряде Фибоначчи: => {count}.')
        break
    count += 1
    (f1, f2) = (f2, f2 + f1)
else:
    print('-1')