def eea(mod, num):  # eea function
    #print("---------------------------");
    #print("eea({}, {}):".format(mod, num));
    r = [mod, num];
    t = [0, 1];
    q = [0];
    i = 1;
    #print("Runde {}: r0 = {}, r1 = {}, t0 = {}, t1 = {}, q0 = {}".format(i, r[0], r[1], t[0], t[1], q));
    while(True):
        i += 1;
        r.append(r[i - 2] % r[i - 1]);
        q.append((r[i - 2] - r[i]) / r[i - 1]);
        t.append(t[i - 2] - q[i - 1] * t[i - 1]);
        #print("Runde {}: r{} = {}, t{} = {}, q{} = {}".format(i, i, r[i], i, t[i], i - 1 , q[i - 1]));
        if(r[i] == 0):
            break;
    #print("---------------------------");
    return int(t[i - 1]);


def computePoint(point1, x2, s, p):  # computes the new point
    x3 = (s ** 2 - point1[0] - x2) % p;  # new x
    y3 = (s * (point1[0] - x3) - point1[1]) % p;  # new y
    # print("newX = ({}^2 - {} - {}) mod {} = {}".format(s, point1[0], x2, p, x3));
    # print("newY = ({}({} - {}) - {}) mod {} = {}".format(s, point1[0], x3, point1[1], p, y3));
    # print("--------------------------------------");
    return (int(x3), int(y3));


def doublePoint(point, a, p):  # double the given point
    # print("--------------------------------------");
    #print("{} + {}:".format(point, point));
    s = (eea(p, 2 * point[1]) * (3 * point[0] ** 2 + a)) % p;  # computes s
    # print("s = ((3 * {}^2 + {}) * (2 * {})^-1) mod {} = {}".format(point[0], a, point[1], p, s));
    return computePoint(point, point[0], s, p);  # returns the computed point

def addPoint(point1, point2, p):  # adds a point to another point 
    # print("--------------------------------------");
    # print("{} + {}:".format(point1, point2));
    # if one of the points is the infinitive point it returns the other point
    if(point1 == 0): 
        return point2;
    elif(point2 == 0):
        return point1;

    else:
        # tests if the point to compute the infinitiv point
        if((point1[0] == point2[0]) and (-point1[1] % p == point2[1])):
            print("Dieser ist Punkt im Unentlichen");
            return 0;
        else:
            # the x2 has to be bigger then x1 otherwise there will be a negative input for the eea 
            # If thats not the case the points have to change
            if(point1[0] > point2[0]): 
                tmpPoint = point1;
                point1 = point2;
                point2 = tmpPoint;

            s = (eea(p, point2[0] - point1[0]) * (point2[1] - point1[1])) % p;  # computes s
            # print("s = (({} - {}) * ({} - {})^-1) mod {} = {}".format(point2[1], point1[1], point2[0], point1[0], p, s));
            return computePoint(point1, point2[0], s, p);  # returns the computed point

    
P = (0,6);
Q = (7,11);
p = 17;
a = 2;
rList = [2, 3, 16, 17];


for r in rList:
    print("for r = {}:".format(r));
    newS = doublePoint(P, a, p);
    for i in range(2, r):
        newS = addPoint(newS, P, p);
    newS = newS[0];
    print("s+1 = {}".format(newS));

    newR = doublePoint(P, a, p);
    for i in range(2, newS):
        newR = addPoint(newR, P, p);
    newR = newR[0];
    print("r+1 = {}".format(newR));

    newT = doublePoint(Q, a, p);
    for i in range(2, newR):
        newT = addPoint(newT, Q, p);
    newT = newT[0];
    print("t+1 = {}".format(newT));

    newO = newT & 0b0111;
    print("o+1 = {}".format(newO));
    print("")