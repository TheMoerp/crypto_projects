from random import randint

def sqmul(base, exp, mod):
    tmpBase = base
    #print("---------------------------")
    #print("SQMUL: {}^{} mod {}".format(base, exp, mod))
    #print("")
    for i in bin(exp)[3:]:
        if(i == '1'):
            tmpBase *= tmpBase
            tmpBase *= base
            #print("{:>3}  SQMUL".format(tmpBase%mod))
        else:
            tmpBase *= tmpBase
            #print("{:>3}  SQ".format(tmpBase%mod))
    #print("---------------------------")
    return tmpBase%mod


# give '' as kb_pr and ka_pr to choose random k_pr's
def dhke(p, alpha, ka_pr, kb_pr):
    # computes k_pr's, k_pub's and k_AB
    if ka_pr == '':
        ka_pr = randint(2, p-1)
    if kb_pr == '':
        kb_pr = randint(2, p-1)
    ka_pub = sqmul(alpha, ka_pr, p)
    kb_pub = sqmul(alpha, kb_pr, p)
    k_AB = sqmul(kb_pub, ka_pr, p)

    # Alice output
    print(f'{"Alice"}'.center(28, '-'))
    print(f'k_pr: {ka_pr}')
    print(f'k_pub: {alpha}^{ka_pr} mod {p} = {ka_pub}')
    print(f'k_AB: {kb_pub}^{ka_pr} mod {p} = {k_AB}')
    print(28*'-')
    print()
    # Bob output
    print(f'{"Bob"}'.center(28, '-'))
    print(f'k_pr: {kb_pr}')
    print(f'k_pub: {alpha}^{kb_pr} mod {p} = {kb_pub}')
    print(f'k_AB: {ka_pub}^{kb_pr} mod {p} = {k_AB}')
    print(28*'-')


def main():
    print()
    print(f'{"Paramter"}'.center(28, '-'))
    p = int(input('p: '))
    alpha = int(input('alpha: '))
    ka_pr = int(input('ka_pr (blank -> random): '))
    kb_pr = int(input('kb_pr (blank -> random): '))
    print(28*'-')
    print('\n')
    dhke(p, alpha, ka_pr, kb_pr)
    print('')

if __name__ == "__main__":
    main()