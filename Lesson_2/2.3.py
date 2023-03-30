import os
os.system('cls')

N = int(input('Введите N:  '))

count = MaxDays = 0

for i in range (N):
    temp = int(input(f"температура в {i+1} день: "))
    if temp > 0:
        count += 1
        if count > MaxDays:
            MaxDays = count
    else:
        count = 0
print(f'Количество теплых дней: {MaxDays}')