def keyAddition(inputMatrix, keyMatrix):
    outputMatrix = []
    for i in range(4):
        curOutputRow = []
        for j in range(4):
            curOutputRow.append(inputMatrix[i][j] ^ keyMatrix[i][j])
        outputMatrix.append(curOutputRow)

    return outputMatrix