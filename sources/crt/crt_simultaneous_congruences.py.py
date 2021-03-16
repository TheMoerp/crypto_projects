from eea import eea

def compute_m(n_i, e, c_i):
    N = 1
    for cur_n in n_i:
        N *= cur_n
    N_i = list(map(lambda x : N // x), n_i)
    inv_N_i = list(map(lambda x, y : eea(x, y), n_i, N_i))
    c = sum([c_i[i] * inv_N_i * N_i for i in range(len(c_i))]) % N
    m = round(c ** (1 / e))
    return m


def main():
    n_i = [int(i) for i in input('Enter the known n eg.: 1,3,4,1,...: ').split(',')]
    e = int(input('Enter e: '))
    c_i = [int(i) for i in input('Enter the known c eg.: 1,3,4,1,...: ').split(',')]
    print(compute_m(n_i, e, c_i))

if __name__ == "__main__":
    main()