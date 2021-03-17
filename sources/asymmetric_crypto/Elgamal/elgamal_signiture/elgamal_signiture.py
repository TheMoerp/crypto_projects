from random import randint
from ggt import ggt
from eea import eea


def sign(p, alpha, k_pr, unsigned_text):
    beta = (alpha ** k_pr) % p
    k_E = 0
    while True:
        k_E = randint(2, p)
        if ggt(k_E, p - 1) == 1:
            break
    r = (alpha ** k_E) % p
    s = (unsigned_text - k_pr * r) * eea(p, k_E)
    return ((p, alpha, beta), (unsigned_text, r, s))


def verify(k_pub, signed_text):
    p, alpha, beta = k_pub
    x, r, s = signed_text
    t = (beta ** r * r ** s) % p
    return (alpha ** x) % p == t


def elgamal_digital_signiture(p, alpha, d, usigned_text):
    k_pub, signed_text = sign(p, alpha, d, usigned_text)
    verification = verify(k_pub, signed_text)
    if verification:
        print('The Message was from Bob')
    else:
        print('The Message was not from Bob')