from squere_multiply import sqmul
from eea import eea

def fake_signiture(i, j, p, alpha, beta):
    r = (sqmul(alpha, i, p) * sqmul(beta, j, p)) % p
    s = (-r * eea((p - 1), j)) % (p - 1)
    x = s * i % (p - 1)
    print("")
    print("r: ({}^{} * {}^{}) mod {} = {}".format(alpha, i, beta, j, p, r))
    print("s: (-{} * {}^-1) mod ({} - 1) = {}".format(r, j, p, s))
    print("x: ({} * {}) mod ({} - 1) = {}".format(s, i, p, x))
    print("")
    return (x, r, s)


fake_signiture(17, 11, 137, 29, 131)
