from constants import BYTE_LENGTH
MATRIX_ROW_CNT = 4


def buildMatrix(inputVal, numberOfBits):
    valStr = "{:0>{}b}".format(inputVal, numberOfBits)
    matrixColumnCnt = int((numberOfBits / BYTE_LENGTH) / MATRIX_ROW_CNT)
    outputMatrix = []

    byteCnt = 0
    for i in range(matrixColumnCnt):
        newRow = []
        for j in range(MATRIX_ROW_CNT):
            newRow.append(int(valStr[byteCnt:byteCnt + BYTE_LENGTH], 2))
            byteCnt += BYTE_LENGTH
            
        outputMatrix.append(newRow)

    outputMatrix = switchMatrixAlignment(outputMatrix)
    return outputMatrix


def printMatrix(matrix, header):
    print("\n{}:".format(header))
    for curRow in matrix:
        print(["{:0>2s}".format(hex(curByte)[2:].upper()) for curByte in curRow])
    print("\n")


def switchMatrixAlignment(inputMatrix):
    outputMatrix = []

    for i in range(len(inputMatrix[0])):
        newSubList = []
        for curSubList in inputMatrix:
            newSubList.append(curSubList[i])
        outputMatrix.append(newSubList)

    return outputMatrix