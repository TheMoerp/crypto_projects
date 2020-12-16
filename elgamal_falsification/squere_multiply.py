def sqmul(base, exp, mod):
    tmpBase = base;
    x = 1;
    # print("---------------------------");
    # print("SQMUL: {}^{} mod {}".format(base, exp, mod));
    # print("");
    for i in bin(exp)[3:]:
        if(i == '1'):
            tmpBase *= tmpBase;
            tmpBase *= base;
            # print("{:>3}  SQMUL".format(tmpBase%mod));
        else:
            tmpBase *= tmpBase;
    #         print("{:>3}  SQ".format(tmpBase%mod));
    # print("---------------------------");
    return tmpBase%mod;