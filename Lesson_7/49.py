
orbits = [(1,3),(2.5,10),(7,2),(6,6),(4,3)]
print(orbits)

def find_far_orbit(x):
    d = dict((3.14*i[0] * i[1], i) for i in x if i[0] != i[1])
    return  d[max(d, key=d.get)]


# def find_far_orbit(x):
#     squears = list([3.14 * i[0] * i[1] for i in x if i[0] != i[1]])
#     return orbits[squears.index(max(squears))]
#
print('Результат => ', *find_far_orbit(orbits))