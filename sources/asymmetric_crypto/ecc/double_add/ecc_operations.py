from eea import eea


def compute_point(point1, x2, s, p):
    x3 = (s ** 2 - point1[0] - x2) % p
    y3 = (s * (point1[0] - x3) - point1[1]) % p
    print(f'newX = ({s}^2 - {point1[0]} - {x2}) mod {p} = {x3}\n'\
          f'newY = (s({point1[0]} - {x3}) - {point1[1]}) mod {p} = {y3}\n'\
          f'The new point is ({x3},{y3})\n{40*"-"}\n')
    return (x3, y3)


def point_doubling(point, a, p):
    s = (eea(p, 2 * point[1]) * (3 * point[0] ** 2 + a)) % p
    print(f'\n{40*"-"}\n{point} + {point}:\ns = ((3 * {point[0]}^2 + {a}) * (2 '\
          f'* {point[1]}^-1) mod {p} = {s}')
    return compute_point(point, point[0], s, p)


def point_addition(point1, point2, p):
    if point1 == 0:
        return point2
    elif point2 == 0:
        return point1
    else:
        if point1[0] == point2[0] and -point1[1] % p == point2[1]:
            print("You are trying to reach the point in the infinite")
            return 0
        else:
            if point1[0] > point2[0]:
                point1, point2 = point2, point1
            s = (eea(p, point2[0] - point1[0]) * (point2[1] - point1[1])) % p
            print(f's = (({point2[1]} - {point1[1]}) * ({point2[0]} - {point1[0]}'\
                  f')^-1) mod {p} = {s}')
            return compute_point(point1, point2[0], s, p)