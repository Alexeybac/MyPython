from itertools import groupby

baals = [len(list(v)) for ch, v in groupby(input().split())]
print(baals)

print(list([i for i in baals if i > 2]))
