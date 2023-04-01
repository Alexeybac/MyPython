
data = list(x for x in range(1,10,2))
print(data)

res = list(filter(lambda x: x % 10 == 5, data))
print(res)

list1 = list(enumerate(data))
print(list1)
list_1 = list(map(lambda x: (x[0]+1, x[1]), list1))
print(list_1)
