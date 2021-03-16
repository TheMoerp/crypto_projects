def eea(mod, num):
    r = [mod, num]
    t = [0, 1]
    q = [0]
    i = 1
    while True:
        i += 1
        r.append(r[i - 2] % r[i - 1])
        q.append(int((r[i - 2] - r[i]) / r[i - 1]))
        t.append(t[i - 2] - q[i - 1] * t[i - 1])
        if r[i] == 0:
            break
    invNum = t[i - 1]
    while invNum < 0:
        invNum = invNum + mod
    return invNum