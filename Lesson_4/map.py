
# map(манипуляции с объектом,  сам объект)
# ========================================
list_1 = [x for x in range(1, 20)]
print(list_1)
list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)

# ========================================
data = '12    45 437  84  63 96 75 05 6  8'
print(type(data))

data = list(map(int, data.split()))
print(data)
print(type(data))