a1, d, n = int(input()), int(input()), int(input())
progressive = [a1 + (i - 1) * d for i in range(1, n + 1)]
print(*progressive)