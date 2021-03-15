from eea import eea


def computePoint(point1, x2, s, p):
    x3 = int((s ** 2 - point1[0] - x2) % p)
    y3 = int((s * (point1[0] - x3) - point1[1]) % p)
    # print("newX = ({}^2 - {} - {}) mod {} = {}".format(s, point1[0], x2, p, x3))
    # print("newY = ({}({} - {}) - {}) mod {} = {}".format(s, point1[0], x3, point1[1], p, y3))
    # print("--------------------------------------")
    return (x3, y3)


def doublePoint(point, a, p):  # double the given point
    # print("--------------------------------------")
    print("{} + {}:".format(point, point))
    s = (eea(p, 2 * point[1]) * (3 * point[0] ** 2 + a)) % p  # computes s
    # print("s = ((3 * {}^2 + {}) * (2 * {})^-1) mod {} = {}".format(point[0], a, point[1], p, s))
    return computePoint(point, point[0], s, p)  # returns the computed point

def addPoint(point1, point2, p):  # adds a point to another point 
    # print("--------------------------------------")
    # print("{} + {}:".format(point1, point2))
    # if one of the points is the infinitive point it returns the other point
    if(point1 == 0): 
        return point2
    elif(point2 == 0):
        return point1

    else:
        # tests if the point to compute the infinitiv point
        if((point1[0] == point2[0]) and (-point1[1] % p == point2[1])):
            print("Dieser ist Punkt im Unentlichen")
            return 0
        else:
            # the x2 has to be bigger then x1 otherwise there will be a negative input for the eea 
            # If thats not the case the points have to change
            if(point1[0] > point2[0]): 
                tmpPoint = point1
                point1 = point2
                point2 = tmpPoint

            s = (eea(p, point2[0] - point1[0]) * (point2[1] - point1[1])) % p  # computes s
            # print("s = (({} - {}) * ({} - {})^-1) mod {} = {}".format(point2[1], point1[1], point2[0], point1[0], p, s))
            return computePoint(point1, point2[0], s, p)  # returns the computed point


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

