str = 'пара-ра-рам рам-пам-парам па-ра-па-дам'
# ===========================================
# def Vinni(x):
#     x = list(str.lower().split())
#     glas = list('аеёиоуыэюя')
#     if len(set([sum(i.count(j) for j in glas) for i in x]))-1:
#         return print('Пам парам')
#     else:
#         return print('Парам пам-пам')
# Vinni(str)
# ==================Все в одну строку========
print('Пам парам'
    if len(set([sum(i.count(j) for j in list('аеёиоуыэюя'))
         for i in list(str.lower().split())])) - 1
        or all([sum(i.count(j) for j in list('аеёиоуыэюя'))
         for i in list(str.lower().split())]) == False
    else
      'Парам пам-пам')
