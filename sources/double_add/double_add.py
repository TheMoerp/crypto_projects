from eea import eea


def computePoint(point1, x2, s, p):
    x3 = (s ** 2 - point1[0] - x2) % p
    y3 = (s * (point1[0] - x3) - point1[1]) % p
    print(f'newX = ({s}^2 - {point1[0]} - {x2}) mod {p} = {x3}\n'\
           'newY = ({s({point1[0] - {x3}) - {point1[1]}) mod {p} = {y3}'\
           '{40*"-"')
    return (x3, y3)


def doublePoint(point, a, p):
    print(f'{40*"-"}\n{point} + {point}:')
    s = (eea(p, 2 * point[1]) * (3 * point[0] ** 2 + a)) % p
    print(f's = ((3 * {point[0]}^2 + {a}) * (2 * {point[1]}^-1) mod {p} = {s}')
    return computePoint(point, point[0], s, p)


def addPoint(point1, point2, p):
    print(f'{40*"-"}\n{point1} + {point2}:')
    if point1 == 0: 
        return point2
    elif point2 == 0:
        return point1
    else:
        if point1[0] == point2[0] and -point1[1]%p == point2[1]:
            print("Dieser ist Punkt im Unentlichen")
            return 0
        else:
            if point1[0] > point2[0]:
                point1, point2 = point2, point1
            s = (eea(p, point2[0] - point1[0]) * (point2[1] - point1[1])) % p
            print(f's = (({point2[1]} - {point1[1]}) * ({point2[0]} - {point1[0]}'\
                   ')^-1) mod {p} = {s}')
            return computePoint(point1, point2[0], s, p)


def dblAdd(startPnt, factor, p, a):
    tmpPnt = startPnt
    print("---------------------------")
    print("DoubleAndAdd: {}{}:".format(factor, startPnt))
    print("")
    for i in bin(factor)[3:]:
        if(i == '1'):
            tmpPnt = doublePoint(tmpPnt, a, p)
            tmpPnt = addPoint(tmpPnt, startPnt, p)
            # tmpPnt *= tmpPnt
            # tmpPnt *= startPnt
            print("{}  DoubleAndAdd".format(tmpPnt))
        else:
            tmpPnt = doublePoint(tmpPnt, a, p)
            print("{}  Double".format(tmpPnt))
    print("---------------------------")
    return tmpPnt

