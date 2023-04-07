
def rev(num):
    if num == 0: return ''
    nums = input()
    return rev(num-1) + f'{nums} '

print(rev(int(input())))