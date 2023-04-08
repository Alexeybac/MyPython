import os
os.system('cls')

nums = list(map(int, input('Введем оценки: ').split()))
print(*nums)
def max1(num):
    dwn = min(num)
    up = max(num)
    return [up, dwn]

print(*(max1(nums)[1] if i == max1(nums)[0] else i for i in nums))


