def Print_operation_table(Oper, num_rous=3, num_columns=6):
    for i in range(1, num_rous + 1):
        for j in range(1, num_columns + 1):
            print(f'{Oper(i, j): 4}', end=' ')
        print()

Print_operation_table(lambda x, y: x * y)
