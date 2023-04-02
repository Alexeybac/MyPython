
# Открытие/создание(при отсутствии) и закрытие файла через переменную:
import os
os.system('cls')

Names = ('Леха','Таня','Варя','Илюха')

with open('File.txt', 'w', encoding= 'utf-8') as date:
    for i in Names:
        date.write(f'Привет {i}\n')
