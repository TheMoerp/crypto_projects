def sqmul(base, exp, mod):
    tmpBase = base
    for i in bin(exp)[3:]:
        if(i == '1'):
            tmpBase *= tmpBase
            tmpBase *= base
        else:
            tmpBase *= tmpBase
    return tmpBase%mod