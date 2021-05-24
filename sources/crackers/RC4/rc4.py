def ksa(N, K):
    print("\n{:-^35}".format(' KSA '))
    S = []
    for i in range(N):
        S.append(i)
    j = 0
    l = len(K)
    for i in range(N):
        j = (j + S[i] + K[i%l]) % N
        S[i], S[j] = S[j], S[i]
        print(f"i={i} j={j}  S={S}")
    print("{:-^35}\n".format(''))
    return S


def prga(N, S):
    print("{:-^43}".format(' PRGA '))
    j = 0
    i = 0
    key = ''
    for k in range(N):
        i = (i + 1) % N
        j = (j + S[i]) % N
        S[i], S[j] = S[j], S[i]
        z = S[(S[i]+S[j])%N]
        key += str(z)
        print(f"i={i} j={j}  S={S} => z{k}={z}")
    print("{:-^43}\n".format(''))
    return key


def rc4(N, K):
    print("<{:=^43}>".format(' RC4 '))
    key = prga(N, ksa(N, K))
    print("<{:=^43}>\n".format(''))
    return key


def main():
    K = [5, 7, 6, 2, 1]
    N = 8
    rc4(N, K)

if __name__ == "__main__":
    main()