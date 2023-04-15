from os import path

file_base = "base.txt"
all_data = []
if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

def read_file():
    global all_data
    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        return all_data

def show_all():
    print()
    [print(i) for i in read_file()]
    print()

def add_rec():
    id = 0
    n = input("Введите Фамилия Имя и Отчество через пробел: ")
    m = input('Введите номер телефона: ')
    x = read_file()
    print(x)
    if x:
        id = int(read_file()[-1][0])
    c = f'{id + 1} {n} {m}'
    new = read_file()
    new.append(c)
    print(new)
    with open(file_base, "w", encoding="utf-8") as f:
        [f.write(str(i) + '\n') for i in new]

def del_rec():
    show_all()
    dell = input('Введите номер удаляемой строки: ')
    rezult = [i for i in read_file() if i[0] != dell]
    id = 1
    rez = []
    for i in rezult:
        rez.append(f'{id}{i[1:]}')
        id += 1

    with open(file_base, "w", encoding="utf-8") as f:
        [f.write(str(i) + '\n') for i in rez]

def find_rec():
    find_str = input('Введите первые 3 буквы имени искомого телефона: ').upper()
    rezult = [i for i in read_file() if find_str in i.upper()]
    print()
    [[print(i) for i in rezult] if rezult else print('Записи с таким вариантом букв не найдены!'.upper())]
    print('==========Конец поиска=============')

def main_menu():
    flag = True
    print(read_file())
    while flag:
        menu = input('Телефонный справочник!\n'
                     '1. Просмотреть весь список\n'
                     '2. Добавить запись\n'
                     '3. Удалить запись\n'
                     '4. Найтить запись\n'
                     '5. Выход\n'
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
                flag = False
            case _:
                print('Непонятный выбор, попробуйте заново\n'.upper())

main_menu()

# 1 Бакшин Алексей Валерьевич 89652906411
# 2 Бакшин Илья Алексеевич 89995554433
# 3 Бакшина Татьяна Александровна 89169604372
# 4 Бакшина Варвара Алексеевна 89003335555
# 5 Бакшин Алексей Валерьевич 89175880683