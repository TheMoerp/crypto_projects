from random import randint
from squere_multiply import sqmul


# give '' as kb_pr and ka_pr to choose random k_pr's
def dhke(p, alpha, ka_pr, kb_pr):
    print(f'{"DHKE"}'.center(28, '-'))
    if ka_pr == '':
        ka_pr = randint(2, p - 1)
    if kb_pr == '':
        kb_pr = randint(2, p - 1)
    ka_pub = sqmul(alpha, ka_pr, p)
    kb_pub = sqmul(alpha, kb_pr, p)
    k_AB = sqmul(kb_pub, ka_pr, p)
    print(f'Alice:\n   k_pr: {ka_pr}\n   k_pub: {ka_pub}\n   k_AB: {k_AB}\n'\
          f'Bob:\n   k_pr: {kb_pr}\n   k_pub: {kb_pub}\n   k_AB: {k_AB}\n'\
          f'{28*"-"}')


def main():
    print()
    print(f'{"Paramter"}'.center(28, '-'))
    p = int(input('p: '))
    alpha = int(input('alpha: '))
    ka_pr = int(input('ka_pr (blank -> random): '))
    kb_pr = int(input('kb_pr (blank -> random): '))
    print(28 * '-')
    print('')
    dhke(p, alpha, ka_pr, kb_pr)
    print('')

if __name__ == "__main__":
    main()