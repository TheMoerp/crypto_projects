alpha = 34 
beta = 182
m = 16
g = 233

def eea(mod, num):
    r = [mod, num]
    t = [0, 1]
    q = [0]
    i = 1
    while(True):
        i += 1
        r.append(r[i - 2] % r[i - 1])
        q.append((r[i - 2] - r[i]) / r[i - 1])
        t.append(t[i - 2] - q[i - 1] * t[i - 1])
        if(r[i] == 0):
            break
    return t[i - 1]

babyStepList = []
giantStepList = []

for i in range(m):
    babyStepList.append(((alpha ** i) % g , i))
giantAlpha = eea(g, (alpha ** m) % g)
for j in range(m):
    giantStepList.append((((giantAlpha ** j) * beta) % g, j))


for k in babyStepList:
    for l in giantStepList:
        if(k[0] == l[0]):
            xb = k[1]
            xg = l[1]
            x = xg * m + xb
            print("{} = {} * {} + {}".format(x, xg, m, xb))
            print("x = {}".format(x))