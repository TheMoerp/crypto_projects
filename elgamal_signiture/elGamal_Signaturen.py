from squere_multiply import sqmul
from eea import eea
from ea import ea


def testKE(ke, p):
    testVal = ea(ke, (p - 1));
    if (testVal == 1):
        return True;
    else: 
        return False;


def signature(alpha, ke, p, d, x):
    print("Signature:");
    r = int(sqmul(alpha, ke, p)); # mod p is in sqmul
    s = int(((x - d * r) * eea((p - 1), ke))) % (p - 1);
    print("r: {}^{} mod {} = {}".format(alpha, ke, p, r));
    print("s: (({} - {} * {}) * {}^-1) mod {} = {}".format(x, d, r, ke, (p - 1), s)); 
    return (r, s);


def verification(x, r, s, p, beta, alpha):
    print("Verification:");
    t = (sqmul(beta, r, p) * sqmul(r, s, p)) % p;
    testVal = sqmul(alpha, x, p);
    print("t: ({}^{} * {}^{}) mod {} = {}".format(beta, r, r, s, p, t));
    print("alpha^x: {}^{} mod {} = {}".format(alpha, x, p, testVal));
    if (t == testVal):
        return True;
    else:
        return False;


p = 137
alpha = 29
beta = 131
x = 119
r = 59
s = 7

print("")
verification(x, r, s, p, beta, alpha)
print("")