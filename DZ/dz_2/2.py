s = int(input())
p = int(input())
num_1 = 1

while num_1 < p:
    num_2 = s - num_1
    if s == num_1 + num_2 and p == num_2 * num_1:
        print(num_1, num_2)
        break
    num_1 += 1