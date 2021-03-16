def eea(mod, num):
    #print("---------------------------")
    #print("eea({}, {}):".format(mod, num))
    r = [mod, num]
    t = [0, 1]
    q = [0]
    i = 1
    #print("Runde {}: r0 = {}, r1 = {}, t0 = {}, t1 = {}, q0 = {}".format(i, r[0], r[1], t[0], t[1], q))
    while(True):
        i += 1
        r.append(r[i - 2] % r[i - 1])
        q.append((r[i - 2] - r[i]) / r[i - 1])
        t.append(t[i - 2] - q[i - 1] * t[i - 1])
        #print("Runde {}: r{} = {}, t{} = {}, q{} = {}".format(i, i, r[i], i, t[i], i - 1 , q[i - 1]))
        if(r[i] == 0):
            break
    #print("---------------------------")
    return t[i - 1]



