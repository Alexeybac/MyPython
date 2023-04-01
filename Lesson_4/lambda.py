# lambda 'возвращаемое значение' : условие или тело функции,

nums = [1, 2, 3, 5, 8, 15, 23, 38]
print(nums)
# rez = list()
# rez = [(i, i*i) for i in nums if i%2 == 0]
# print(rez)


def cel(f, list):
    return [f(x) for x in list]

def chet(f, list):
    return [x for x in list if f(x)]

rez = cel(int, nums)
print(rez)

rez = chet(lambda x: x % 2 == 0, cel(int, nums))
print(rez)

rez = cel(lambda x: (x, x**2), rez)
print(rez)

