from matrixManager import buildMatrix
from substitutionLayer import sBox
from diffusionLayer import shiftRows, mixColumn, getMatrixVal
from keyAdditionLayer import addKey

KEY = 0xE9A6EC1C7CBB2868A996A6E532DED24B
KEY1 = 0xF5135F3F89A87757203ED1B212E003F9
INPUT = 0x00000000000000000000010000000000

# KEY = 0x2b7e151628aed2a6abf7158809cf4f3c
# KEY1 = 0xa0fafe1788542ab123a339392a6c7605
# INPUT = 0x3243f6a8885a308d313198a2e0370734


# def aesRound(inputVal, aesSize, keyVal):
#     return addKey(
#                 mixColumn(
#                     shiftRows(
#                         sBox(
#                             buildMatrix(inputVal, aesSize)
#                         )
#                     )
#                 ),
#            inputKey)


print("\nkeyAddition mit k0:")
matrix = buildMatrix(addKey(INPUT, KEY), 128)
for i in matrix:
    i = ["{:0>2s}".format(hex(j)[2:].upper()) for j in i]
    print(i)

print("\nbyteSubstitution:")
matrix = sBox(matrix)
for i in matrix:
    i = ["{:0>2s}".format(hex(j)[2:].upper()) for j in i]
    print(i)

print("\nshiftRow:")
matrix = shiftRows(matrix)
for i in matrix:
    i = ["{:0>2s}".format(hex(j)[2:].upper()) for j in i]
    print(i)



print("\nmixColumn:")
matrix1 = buildMatrix(mixColumn(matrix), 128)
for i in matrix1:
    i = ["{:0>2s}".format(hex(j)[2:].upper()) for j in i]
    print(i)

print("\nkeyAddition mit k1:")
matrix = buildMatrix(addKey(mixColumn(matrix), KEY1), 128)
for i in matrix:
    i = ["{:0>2s}".format(hex(j)[2:].upper()) for j in i]
    print(i)


bitCnt = 0


for i in bin(INPUT ^ getMatrixVal(matrix)):
    bitCnt = bitCnt + 1 if i == "1" else bitCnt 

print("\nAnzahl an geänderten Bits: {}\n".format(bitCnt))
