N = 20
A = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

MIN = 1
MAX = 19
for i in range(N):
    if MIN <= A[i] <= MAX:
        print(i, end = ' ')