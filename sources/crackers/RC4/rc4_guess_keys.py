from rc4 import rc4

def ksa(N, K, cur_i):
    print("\n{:-^35}".format(' KSA '))
    S = []
    j_list = []
    for i in range(N):
        S.append(i)
    j = 0
    l = len(K)
    for i in range(cur_i):
        j = (j + S[i] + K[i%l]) % N
        j_list.append(j)
        S[i], S[j] = S[j], S[i]
        print(f"i={i} j={j}  S={S}")
    print("{:-^35}\n".format(''))
    return S, j_list


def guess_keys(N, K, cur_i, z):
    print("\n<{:=^43}>".format(' ATTACK '))
    S, j_list = ksa(N, K, cur_i)
    for i in range(N):
        if S[i] == z:
            j_list.append(i)
            break
    k_part = (j_list[cur_i] - j_list[cur_i-1] - S[cur_i]) % N
    K.append(k_part)
    print(f"K[{cur_i}]={K[cur_i]}")
    print(f"Complete K may be: {K}\n")
    print("<{:=^43}>\n".format(''))
    return K



def main():
    K = [4, 7, 5, 5]
    N = 8
    cur_i = 4
    z = 6

    K = guess_keys(N, K, cur_i, z)
    rc4(N, K)

if __name__ == "__main__":
    main()