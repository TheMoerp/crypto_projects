from matrixManager import buildMatrix, printMatrix
from keyAdditionLayer import keyAddition
from substitutionLayer import sBox
from shiftRow import shiftRows
from mixColumn import mixColumn
from constants import ENCRYPT


def aesRound(inputMatrix, keyMatrix, roundInfo, mode): # roundInfo ("bool: lastround", curRound) curround 0 - lastround

    if mode == ENCRYPT:
        if roundInfo[1] == 1:
            matrixAfterKA = keyAddition(matrixAfterMC, keyMatrix)
            printMatrix(matrixAfterKA, "KeyAdditionLayer Round {}".fromat(roundInfo[1] - 1))

        printMatrix(inputMatrix, "RoundStart Round {}".format(roundInfo[1]))

        matrixAfterSL = sBox(inputMatrix, mode)
        printMatrix(matrixAfterSL, "SubstitutionLayer Round {}".format(roundInfo[1]))

        matrixAfterSR = shiftRows(matrixAfterSL, mode)
        printMatrix(matrixAfterSR, "ShiftRows Round {}".format(roundInfo[1]))

        if not roundInfo[0]:
            matrixAfterMC = mixColumn(matrixAfterSR, mode)
            printMatrix(matrixAfterMC, "MixColumns Round {}".format(roundInfo[1]))

        matrixAfterKA = keyAddition(matrixAfterMC, keyMatrix)
        printMatrix(matrixAfterKA, "KeyAdditionLayer Round {}".format(roundInfo[1]))
    else:
        printMatrix(inputMatrix, "RoundStart Round {}".format(roundInfo[1]))

        matrixAfterKA = keyAddition(matrixAfterMC, keyMatrix)
        printMatrix(matrixAfterKA, "KeyAdditionLayer Round {}".format(roundInfo[1]))

        if not roundInfo[0]:
            matrixAfterMC = mixColumn(matrixAfterSR, mode)
            printMatrix(matrixAfterMC, "Inverse MixColumns Round {}".format(roundInfo[1]))

        matrixAfterSR = shiftRows(matrixAfterSL, mode)
        printMatrix(matrixAfterSR, "Inverse ShiftRows Round {}".format(roundInfo[1]))

        matrixAfterSL = sBox(inputMatrix, mode)
        printMatrix(matrixAfterSL, "Inverse SubstitutionLayer Round {}".format(roundInfo[1]))

        if roundInfo[1] == 1:
            matrixAfterKA = keyAddition(matrixAfterMC, keyMatrix)
            printMatrix(matrixAfterKA, "KeyAdditionLayer Round {}".fromat(roundInfo[1] - 1))



# matrixAfterSR = buildMatrix(0, 128)
# printMatrix(matrixAfterSR, "ShiftRows")
# matrixAfterMC = mixColumn(matrixAfterSR, "encrypt")
# printMatrix(matrixAfterMC, "MixColumns")
# matrixAfterKA = keyAddition(matrixAfterMC, buildMatrix(0xD09D621937BCA549A40E8AAD938B22F4, 128))
# printMatrix(matrixAfterKA, "KeyAdditionLayer")