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
    with open(file_base, "r", encoding="utf-8") as f:
        n = input("Введите Фамилия Имя и Отчество через пробел: ")
        m = input('Введите номер телефона: ')
        id = int(read_file()[-1][0])
        c = f'{id+1} {n} {m}'
        new = read_file()
        new.append(c)
        print(new)
    with open(file_base, "w", encoding="utf-8") as f:
        [f.write(str(i)+'\n') for i in new]


def main_menu():
    flag = True
    print(read_file())
    while flag:
        menu = input('Телефонный справочник!\n'
                     '1. Просмотреть весь список\n'
                     '2. Добавить запись\n'
                     '3. Найтить запись\n'
                     '4. Выход\n'
                     'Введите вариант: ')
        match menu:
            case '1':
                show_all()
            case '2':
                add_rec()
            case '3':
                pass
            case '4':
                flag = False
            case _:
                print('Непонятный выбор, попробуйте заново\n'.upper())


main_menu()

# 1 Бакшин Алексей Валерьевич 89652906411
# 2 Бакшин татьяна Александровка 89169604372
