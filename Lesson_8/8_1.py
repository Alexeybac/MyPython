from os import path

file_base = "base.txt"
all_data = []
id = 0
if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

def read_file():
    global all_data
    global id
    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            id = all_data[-1].split()[0]
        return all_data

def show_all():
    print(*all_data, sep='\n')

def add_rec():
    global id
    global all_data
    n = input("Введите Фамилия Имя и Отчество через пробел: ")
    m = input('Введите номер телефона: ')
    c = int(id)
    all_data += [f'{c + 1}  {n} {m}']
    with open(file_base, "w", encoding="utf-8") as f:
        [f.write(i + '\n') for i in all_data]

def del_rec():
    show_all()
    dell = input('Введите номер удаляемой строки: ')
    rezult = [i for i in all_data if not dell in i]
    id = 1
    rez = []
    for i in rezult:
        rez.append(f'{id}  {i[3:]}')
        id += 1
    with open(file_base, "w", encoding="utf-8") as f:
        [f.write(str(i) + '\n') for i in rez]

def find_rec():
    find_str = input('Введите чего нибудь: ').upper()
    rezult = [i for i in all_data if find_str in i.upper()]
    print()
    [[print(i) for i in rezult] if rezult else print('Записи с таким вариантом букв не найдены!'.upper())]
    print('==========Конец поиска=============')

def import_rec():
    global file_base
    old_file = read_file()
    id = 1
    file_base = input('Введите имя файла для импорта: ') + '.txt'
    if not path.exists(file_base):
        print('Такого файла здесь нет!\n')
        file_base = "base.txt"
        return
    for i in read_file():
        old_file.append(i)
    all_data = []
    if len(old_file) >= 1000:
        file_base = "base.txt"
        return print('Размер справочника будет максимальным.')
    for i in old_file:
        all_data.append(f'{id}  {i[3:]}')
        id += 1
    file_base = "base.txt"
    with open(file_base, "w", encoding="utf-8") as f:
        [f.write(i + '\n') for i in all_data]

def export_rec():
    id = 0
    path_file = input('Введите название файла, куда экспортировать данные: ') + '.txt'
    if not path.exists(path_file):
        with open(path_file, "w", encoding="utf-8") as _:
            pass
    with open(path_file, 'r', encoding='utf-8') as f:
        old_data = [line.strip() for line in f]
        if old_data:
            id = int(all_data[-1].split()[0]) + 1
    with open(path_file, 'a', encoding='utf-8') as f:
        rez = []
        if len(old_data) + len(all_data) >= 1000:
            return print('Размер справочника будет максимальным.')
        for i in all_data:
            rez.append(f'{id}  {i[3:]}')
            id += 1
        [f.write(line + '\n') for line in rez]

def off_menu():
    flag = True
    while flag:
        menu = input('<<<Телефонный справочник>>>\n'
                     '1. Импорт из файла\n'
                     '2. Экспорт в файл\n'
                     '3. Выход в верхнее меню\n'
                     'Введите вариант: ')
        match menu:
            case '1':
                import_rec()
            case '2':
                export_rec()
            case '3':
                flag = False
            case _:
                print('Непонятный выбор, попробуйте заново\n'.upper())

def main_menu():
    flag = True
    while flag:
        read_file()
        menu = input('<<<Телефонный справочник>>>\n'
                     '1. Просмотреть весь список\n'
                     '2. Добавить запись\n'
                     '3. Удалить запись\n'
                     '4. Найтить запись\n'
                     '5. Работа со справочником\n'
                     '6. Выход\n'
                     'Введите вариант: ')
        match menu:
            case '1':
                show_all()
            case '2':
                add_rec()
            case '3':
                del_rec()
            case '4':
                find_rec()
            case '5':
                off_menu()
            case '6':
                flag = False
            case _:
                print('Непонятный выбор, попробуйте заново\n'.upper())

main_menu()

# 1 Бакшин Алексей Валерьевич 89652906411
# 2 Бакшин Илья Алексеевич 89995554433
# 3 Бакшина Татьяна Александровна 89169604372
# 4 Бакшина Варвара Алексеевна 89003335555
# 5 Бакшин Алексей Валерьевич 89175880683