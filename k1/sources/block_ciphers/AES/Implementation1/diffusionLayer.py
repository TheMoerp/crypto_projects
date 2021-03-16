from operationInGF import multiplicationGF, additionGF
BYTE_LENGTH = 8

MIX_COLUMN_MATRIX = ((2, 3, 1, 1),
                     (1, 2, 3, 1),
                     (1, 1, 2, 3),
                     (3, 1, 1, 2))



def shiftingFunction(inputRow, shiftCnt):
    rowLength = len(inputRow)
    outputRow = [0] * rowLength
    
    for i in range(rowLength):
        outputRow[(i + shiftCnt) % rowLength] = inputRow[i]

    return outputRow


def shiftRows(inputMatrix):
    outputMatrix = []
    shiftCnt = 0

    for curRow in inputMatrix:
        outputMatrix.append(shiftingFunction(curRow, shiftCnt % len(curRow)))
        shiftCnt -= 1
    
    return outputMatrix


def switchMatrixAlignment(inputMatrix):
    outputMatrix = []

    for i in range(len(inputMatrix[0])):
        newSubList = []
        for curSubList in inputMatrix:
            newSubList.append(curSubList[i])
        outputMatrix.append(newSubList)

    return outputMatrix


def getMatrixVal(inputMatrix):
    valStr = ""
    for curColumn in inputMatrix:
        for curByte in curColumn:
            valStr += "{:0>{}b}".format(curByte, BYTE_LENGTH) 

    return int(valStr, 2)


def matrixMultiplication(curColumnList):
    outputColumn = []

    for curConstRow in MIX_COLUMN_MATRIX:
        curColumnObject = 0

        for i in range(len(curColumnList)):
            curColumnObject = additionGF(curColumnObject, multiplicationGF(curColumnList[i], curConstRow[i]))

        outputColumn.append(curColumnObject)

    return outputColumn


def mixColumn(inputMatrix):
    inputMatrix = switchMatrixAlignment(inputMatrix)
    outputMatrix = []

    for curColumnList in inputMatrix:
        outputMatrix.append(matrixMultiplication(curColumnList))
        
    return getMatrixVal(outputMatrix)


