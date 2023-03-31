import os
os.system('cls')

n = int(input('Введите N '))
txt = list()
for i in range(n):
    txt.append(i+1)
print(txt)
txt1 = txt
k = int(input('Введите K '))
# Через СЛАЙС (копии объекта)
print(txt1[k%len(txt1):] + txt1[:k%len(txt1)])
# Через цикл for
for i in range(0, k): 
    txt.insert(len(txt),txt.pop(0))
print(txt)