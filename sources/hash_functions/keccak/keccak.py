RC = [0x0000000000000001,
      0x0000000000008082,
      0x800000000000808A,
      0x8000000080008000,
      0x000000000000808B,
      0x0000000080000001,
      0x8000000080008081,
      0x8000000000008009,
      0x000000000000008A,
      0x0000000000000088,
      0x0000000080008009,
      0x000000008000000A,
      0x000000008000808B,
      0x800000000000008B,
      0x8000000000008089,
      0x8000000000008003,
      0x8000000000008002,
      0x8000000000000080,
      0x000000000000800A,
      0x800000008000000A,
      0x8000000080008081,
      0x8000000000008080,
      0x0000000080000001,
      0x8000000080008008]

def rot(x, shift_length, word_length):
    shift_length %= word_length
    return ((x >> (word_length - shift_length)) 
             + (x << shift_length)) % (1 << word_length)


def theta(A, word_length):
    C = [0, 0, 0, 0, 0]
    D = [0, 0, 0, 0, 0]
    for x in range(5):
        C[x] = A[x][0] ^ A[x][1] ^ A[x][2] ^ A[x][3] ^ A[x][4]
    for x in range(5):
        D[x] = C[(x - 1) % 5] ^ rot(C[(x + 1) % 5], 1, word_length)
    for x in range(5):
        for y in range(5):
            A[x][y] = A[x][y] ^ D[x]
    return A


def rho_pi(A, word_length):
    rho_table = [[0,  36,   3,  41,  18],
                 [1,  44,  10,  45,   2],
                 [62,  6,  43,  15,  61],
                 [28, 55,  25,  21,  56],
                 [27, 20,  39,   8,  14]]
    B = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]

    for x in range(5):
        for y in range(5):
            B[y][(2 * x + 3 * y) % 5] = rot(A[x][y], rho_table[x][y], word_length)
    return B


def chi(A, B):
    for x in range(5):
        for y in range(5):
            A[x][y] = B[x][y] ^ ((~B[(x + 1) % 5][y]) & B[(x + 2) % 5][y])
    return A


def jota(A, round_const):
    A[0][0] ^= round_const
    return A


def round(A, round_const, word_length):
    A = theta(A, word_length)
    B = rho_pi(A, word_length)
    A = chi(A, B)
    A = jota(A, round_const)
    return A


def f_function(A, round_num, word_length=1600//25):
    for i in range(round_num):
        A = round(A, RC[i] % (1 << word_length), word_length)
    return A