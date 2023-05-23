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


def det(mat):
    """Определитель(детерминант) матрицы"""
    if len(mat[0]) == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

    main = 0
    secondary = 0

    for j in range(len(mat)):
        value = 1
        for i in range(len(mat)):
            value *= mat[i][j]
            j += 1
            if j == len(mat):
                j += - len(mat)
        main += value

    for j in range(len(mat)):
        value = 1
        for i in range(len(mat)):
            value *= mat[i][-(j+1)]
            j += 1
            if j == len(mat):
                j += - len(mat)
        secondary += value

    return main - secondary
