import os
os.system('cls')

def sum(a,b):
    if a: return sum(a - 1, b) + 1
    return  b

print(sum(5,5))