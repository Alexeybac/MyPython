# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X


from random import randint

list_1 = [randint(1, 21) for i in range(int(input()))]
print(list_1)
num = int(input())
num_2 = list_1[0]
for i in list_1:
    if abs(num - i) < abs(num - num_2):
        right_num = i
print(num_2)