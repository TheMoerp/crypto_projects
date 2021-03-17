from random import randint
from eea import eea
from dhke import dhke
from squere_multiply import sqmul


def elgamal_cipher(p, alpha, ka_pr, kb_pr, plaintext):
    print(f'{"Elgamal-cipher"}'.center(38, '-'))
    # In an real life szenario this would work different
    k_M = dhke(p, alpha, ka_pr, kb_pr)
    # Alice
    y = (plaintext * k_M) % p
    # Bob
    x = (y * eea(p, k_M)) % p
    print(f'ciphertext y : {x} * {k_M} mod {p} = {y}\n'\
          f'plaintext x  : {y} * {k_M}^-1 mod {p} = {x}\n'\
          f'{38*"-"}\n')
    return x


def main():
    print()
    print(f'{"Paramter"}'.center(28, '-'))
    p = int(input('p: '))
    alpha = int(input('alpha: '))
    ka_pr = int(input('ka_pr (blank -> random): '))
    kb_pr = int(input('kb_pr (blank -> random): '))
    plaintext = int(input('\nplaintext eg.: 26: '))
    print(f'{28*"-"}\n')
    elgamal_cipher(p, alpha, ka_pr, kb_pr, plaintext)

if __name__ == "__main__":
    main()