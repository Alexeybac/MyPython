n = int(input())
k = 0
for i in range(n):
    v = int(input())
    if v == 1:
        k += 1
print(k if k<n/2 else n-k)