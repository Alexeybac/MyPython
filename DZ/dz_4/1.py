n, m = input().split()
one = [int(i) for i in input().split()]
two = [int(j) for j in input().split()]

print((set(one).intersection(two)))