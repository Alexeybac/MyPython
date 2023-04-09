a = list(int(i) for i in input('Введите числа в массив: ').split())
print(a)

print(sum([a.count(i)//2 for i in set(a)])) # Вариант в строку

# double = []
# count = 0
# for i in range(len(a)-1):
#     for j in range(i + 1, len(a)):
#         if a[i] in double:
#             break
#         if a[i] == a[j]:
#             count += 1
#             double.append(a[i])
# print(double)
# print(count)
