def sqmul(base, exp, mod):
    print(f'{40*"-"}\nSQMUL: {base}^{exp} mod {mod}\n')
    tmp_base = base
    for i in bin(exp)[3:]:
        if(i == '1'):
            tmp_base *= tmp_base
            tmp_base *= base
            print("{:>3}  SQMUL".format(tmp_base % mod))
        else:
            tmp_base *= tmp_base
            print("{:>3}  SQ".format(tmp_base % mod))
    print(40 * '-')
    return tmp_base%mod


def main():
    base = int(input('base: '))
    exp = int(input('exponent: '))
    mod = int(input('mod: '))
    print(sqmul(base, exp, mod))

if __name__ == "__main__":
    main()