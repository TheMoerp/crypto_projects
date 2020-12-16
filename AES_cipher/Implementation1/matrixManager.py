from diffusionLayer import switchMatrixAlignment

MATRIX_ROW_CNT = 4
BYTE_LENGTH = 8


def buildMatrix(inputVal, aesSize):
    valStr = "{:0>{}b}".format(inputVal, aesSize)
    matrixColumnCnt = int((aesSize / BYTE_LENGTH) / MATRIX_ROW_CNT)
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
