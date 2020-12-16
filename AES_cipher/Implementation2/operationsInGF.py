from constants import BYTE_LENGTH
BYTE_MASK = 0b11111111
CONGRUENT_BYTE = 0b11011


def preMultiplication(fac1, fac2):
    result = 0

    for i in range(BYTE_LENGTH):
        if ((fac1 >> i) & 1) == 1:
            result ^= (fac2 << i)

    return result


def reductionInGF(input):
    for i in range(BYTE_LENGTH * 2 - 1, BYTE_LENGTH - 1, -1):
        if ((input >> i) & 1) == 1:
             input ^= (CONGRUENT_BYTE << (i - BYTE_LENGTH)) 

    reductedOutput = input & BYTE_MASK
    return reductedOutput


def multiplicationInGF(fac1, fac2):
    return reductionInGF(preMultiplication(fac1, fac2))


# nr1 = 32
# nr2 = 63
# print("\nMultiplication in GF(2^8):\n0b{:0>8b} * 0b{:0>8b} = 0b{:0>8b}\n0x{} * 0x{} = 0x{}\n".format(nr1, nr2, multiplicationInGF(nr1, nr2), hex(nr1)[2:].upper(), hex(nr2)[2:].upper(), hex(multiplicationInGF(nr1, nr2))[2:].upper()))
