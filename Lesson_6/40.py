# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном
# массиве определит количество элементов,
# у которых два соседних и, при этом,
# оба соседних элемента меньше данного.

# Сначала вводится число N — количество
# элементов в массиве. Далее записаны N
# чисел — элементы массива.
# Массив состоит из целых чисел.
# 1 2 3 4 5
# 1 5 1 4 1
# _ = input()
from time import time
nums = [int(i) for i in input('введите числа: ').split()]
start = time()
print(nums)
count = 0
# for i in range(1, len(nums)-1):
#     if nums[i] == max(nums[i-1:i+2]):
#         count +=1
# print(count)
print(len([i for i in range(1, len(nums)-1) if nums[i] == max(nums[i-1:i+2])]))
print(time()-start)
