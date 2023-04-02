#  Чтение из файла:
import os
os.system('cls')

red = open('File.txt', 'r', encoding= 'utf-8')
for x in red:
    print(x)
red.close()

