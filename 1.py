def gaus_jor(mass):
    """Метод Гаусса — Жордана"""
    for i in range(len(mass)):
        if i == len(mass):
            break
        if all(_ == 0 for _ in mass[i]):
            mass.pop(i)
        try:
            set1 = list(map(lambda x: x/mass[i][i], mass[i]))
        except ZeroDivisionError:
            for j in range(len(mass)):
                if i + j + 1 == len(mass):
                    return False
                if mass[i+j+1][i] != 0:
                    mass[i], mass[i+j+1] = mass[i+j+1], mass[i]
                    set1 = list(map(lambda x: x / mass[i][i], mass[i]))
                    break
        mass[i] = set1
        for j in range(len(mass)):
            if j == i:
                continue
            d = list(map(lambda x: -x*mass[j][i], mass[i]))
            c = list(map(sum, zip(d, mass[j])))
            mass[j] = c
    result = []
    for _ in mass:
        result.append(list(map(lambda x: round(x, 5), _)))
    return result


# a2 = [2, -3, 1, 7]
# a = [3, 0, -1, 6]
# a1 = [4, 7, -3, 4]
# aij = [a, a1, a2]

a = [0, 2, 3, 1, 0, 0]
a1 = [1, 1, 4, 0, 1, 0]
a2 = [2, -1, 3, 0, 0, 1]
aij = [a, a1, a2]

g = gaus_jor(aij)
if g:
    for _ in g:
        print(_)
else:
    print(g)


