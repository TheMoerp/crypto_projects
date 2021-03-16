from constants import ENCRYPT


def shiftingFunction(inputRow, shiftCnt):
    rowLength = len(inputRow)
    outputRow = [0] * rowLength
    
    for i in range(rowLength):
        outputRow[(i + shiftCnt) % rowLength] = inputRow[i]

    return outputRow


def shiftRows(inputMatrix, mode):
    outputMatrix = []
    shiftCnt = 0

    for curRow in inputMatrix:
        outputMatrix.append(shiftingFunction(curRow, shiftCnt % len(curRow)))
        shiftCnt = shiftCnt - 1 if mode == ENCRYPT else shiftCnt + 1
    
    return outputMatrix