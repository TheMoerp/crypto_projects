# Ciffrat ci
c1 = 1786058302
c2 = 521332323
c3 = 2806221682

# Exponent e
e = 3

# Modulo ni
n1 = 3748150753
n2 = 3012222769
n3 = 3715158301

# Berechnung des EEA
def eea(mod, num):
    r = [mod, num]
    t = [0, 1]
    q = [0]
    i = 1
    while True:
        i += 1
        r.append(r[i - 2] % r[i - 1])
        q.append((r[i - 2] - r[i]) / r[i - 1])
        t.append(t[i - 2] - q[i - 1] * t[i - 1])
        if r[i] == 0:
            break
    invNum = t[i - 1]
    while invNum < 0:
        invNum = invNum + mod
    return invNum

# Berechnung von N
N = n1 * n2 * n3

# Berechnung von Ni & Reduzierung von Ni mit ni
N1 = N // n1
N2 = N // n2
N3 = N // n3

# Berechnung der Multiplikativen Inversen von Ni
invN1 = int(eea(n1, N1))
invN2 = int(eea(n2, N2))
invN3 = int(eea(n3, N3))

# Berechnung der simultanen Kongruenz s
c = ((c1 * invN1 * N1) + (c2 * invN2 * N2) + (c3 * invN3 * N3)) % N

# Berechnung des Klartext m in Dezimalschreibweise
m = round(c ** (1 / e))

# Berechne Klartext aus m
m = str(m)
tmpM = [m[::-1][i:i+3] for i in range(0, len(m), 3)][::-1]
mParts = [tmpM[i][::-1] for i in range(len(tmpM))]
decText = ''.join([chr(int(mParts[i])) for i in range(len(mParts))])

# Gebe den Klartext von m aus
print("Der Klartext lautet: {}".format(decText))