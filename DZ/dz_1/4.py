size_1 = int(input())
size_2 = int(input())
slice = int(input())

if (slice == (size_1 or size_2) or slice % (size_1 or size_2) == 0 and slice != (size_1 * size_2)):    
    print('yes')
else: 
    print('no')