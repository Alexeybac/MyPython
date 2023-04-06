import os
os.system('cls')

# Input: She sells sea shells on the sea shore
# The shells that she sells are sea shells
# I'm sure.So if she sells sea shells on
# the sea shore I'm sure that the
# shells are sea shore shells

sting = input('Ведите')
# print(sting)

rezult = len(set((sting.upper()).split()))
print(rezult)