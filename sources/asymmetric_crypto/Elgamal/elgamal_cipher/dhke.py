from random import randint
from squere_multiply import sqmul


def dhke(p, alpha, ka_pr, kb_pr):
    print()
    print(f'{"DHKE"}'.center(28, '-'))
    if ka_pr == '':
        ka_pr = randint(2, p - 1)
    if kb_pr == '':
        kb_pr = randint(2, p - 1)
    ka_pub = (alpha ** ka_pr) % p
    kb_pub = (alpha ** kb_pr) % p
    k_AB = (kb_pub ** ka_pr) % p
    print(f'Alice:\n   k_pr: {ka_pr}\n   k_pub: {ka_pub}\n   k_AB: {k_AB}\n'\
          f'Bob:\n   k_pr: {kb_pr}\n   k_pub: {kb_pub}\n   k_AB: {k_AB}\n'\
          f'{28*"-"}\n')
    return k_AB