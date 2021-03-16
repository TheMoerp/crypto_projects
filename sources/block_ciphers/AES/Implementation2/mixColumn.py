from operationsInGF import multiplicationInGF
from shiftRow import shiftingFunction
from matrixManager import switchMatrixAlignment
from constants import ENCRYPT, DECRYPT

MIX_COLUMN_CONST_ROW = {ENCRYPT : (0x2, 0x3, 0x1, 0x1), DECRYPT : (0xE, 0xB, 0xD, 0x9)}


def matrixMultiplication(curColumnList, constRow):
    outputColumn = []

    for i in range(len(constRow)):
        curConstRow = shiftingFunction(constRow, i)
        curColumnObject = 0
        for i in range(len(curColumnList)):
            curColumnObject = curColumnObject ^ multiplicationInGF(curColumnList[i], curConstRow[i])

        outputColumn.append(curColumnObject)

    return outputColumn


def mixColumn(inputMatrix, mode):
    constRow = MIX_COLUMN_CONST_ROW[mode]
    inputMatrix = switchMatrixAlignment(inputMatrix)
    outputMatrix = []

    for curColumnList in inputMatrix:
        outputMatrix.append(matrixMultiplication(curColumnList, constRow))
        
    outputMatrix = switchMatrixAlignment(outputMatrix)
    return outputMatrix