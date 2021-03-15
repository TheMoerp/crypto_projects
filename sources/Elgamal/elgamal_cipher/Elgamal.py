def sqmul(base, exp, mod):
    tmpBase = base
    x = 1
    print("---------------------------")
    print("SQMUL: {}^{} mod {}".format(base, exp, mod))
    print("")
    for i in bin(exp)[3:]:
        if(i == '1'):
            tmpBase *= tmpBase
            tmpBase *= base
            print("{:>3}  SQMUL".format(tmpBase % mod))
        else:
            tmpBase *= tmpBase
            print("{:>3}  SQ".format(tmpBase % mod))
    print("---------------------------")
    return tmpBase % mod


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
    print("---------------------------")
    print("EEA({}, {}) => Inverse of {} is {}".format(mod, num, num, t[i - 1]))
    print("Km^-1: {}".format(t[i - 1]))
    print("---------------------------")
    return t[i - 1]

def computeKpub(alpha, d, p):
    print("---- Bob computes Kpub ----")
    kpub = sqmul(alpha, d, p)
    print("Kpub: {}".format(kpub))
    print("")
    return kpub

def computeKe(alpha, i, p):
    print("---- Alice computes Ke ----")
    ke = sqmul(alpha, i, p)
    print("Ke: {}".format(ke))
    print("")
    return ke

def computeKmA(kpub, i, p):
    print("---- Alice computes Km ----")
    km = sqmul(kpub, i, p)
    print("Km: {}".format(km))
    print("")
    return km

def encrypt(x, km, p):
    print("---- Alice encrypts x -----")
    y = (x * km) % p
    print("y: {}".format(y))
    print("")
    return y

def computeKmB(ke, d, p):
    print("----- Bob computes Km -----")
    km = sqmul(ke, d, p)
    print("Km: {}".format(km))
    print("")
    return km

def decrypt(y, km, p):
    print("----- Bob decrypts y ------")
    invKm = eea(p, km)
    x = (y * invKm) % p
    print("x: {}".format(x))
    print("")
    return x



alpha = 21
p = 397
d = 175
i = 201
x = 139

print("")
kpub = computeKpub(alpha, d, p)
ke = computeKe(alpha, i, p)
kma = computeKmA(kpub, i, p)
y = encrypt(x, kma, p)
kmb = computeKmB(ke, d, p)
decrypt(y, kmb, p)