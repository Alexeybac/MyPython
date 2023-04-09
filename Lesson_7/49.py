orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(orbits)

def find_far_orbit(x):
    return max((3.14 * i[0] * i[1], i) for i in x if i[0] != i[1])[1]
print('Результат => ', *find_far_orbit(orbits))

