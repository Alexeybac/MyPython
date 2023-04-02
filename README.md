#  MyPython

print('===========================================')
text = 'Улыбок Тебе дед Мокар'
print(text.lower())
print(text.upper())
print(text.replace('дед', 'ДЕД'))
print(text[0:len(text):1])
print(text[len(text):0:-1] + text[0])

print('===========================================')

nums = 1, 2, 3, 4, 5
for i in nums:
    print(i)

print('===========================================')

i = 0
while (i < len(nums)):
    print(nums[i])
    i += 1

print('===========================================')

ear = int(input('Введите проверяемый год: '))
if (ear%4 == 0 and ear%100 != 0) or ear%400 == 0:
    print('Високосный!')

    She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells