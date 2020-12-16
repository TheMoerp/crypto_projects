from operationsInGF import reductionInGF
from KeyPlanFunctions import gFunction, hFunction
from matrixManager import printMatrix, buildMatrix, switchMatrixAlignment
from constants import ENCRYPT, DECRYPT


def computeRoundCounterArray(nrOfRounds): 
    rCArray = []
    for i in range(nrOfRounds):
        rCArray.append(reductionInGF(1 << i))
    
    return rCArray


def xorWords(inputWord1, inputWord2):
    outputWord = []
    for j in range(len(inputWord1)):
        outputWord.append(inputWord1[j] ^ inputWord2[j])

    return outputWord


def appendRoundKey(destinationList, inputMatrix):
    for curWord in inputMatrix:
        destinationList.append(curWord)
    return destinationList


def keyPlanRound(inputMatrix, curRC, keySize, mode): # für 192&256 müssen mindestens 6words bzw 8words bekannt sein für decryption
    inputMatrixLength = len(inputMatrix)
    outputMatrix = inputMatrix

    if mode == ENCRYPT:
        for i in range(inputMatrixLength):
            if i == 0:
                outputMatrix[i] = xorWords(gFunction(inputMatrix[inputMatrixLength - 1], curRC), inputMatrix[i])
            elif keySize == 256 and i == 4:
                outputMatrix[i] = xorWords(hFunction(outputMatrix[i - 1]), inputMatrix[i])
            else:
                outputMatrix[i] = xorWords(inputMatrix[i], outputMatrix[i - 1])
    else:
        for i in range(inputMatrixLength - 1, -1, -1):
            if i == 0:
                outputMatrix[i] = xorWords(gFunction(outputMatrix[inputMatrixLength - 1], curRC), inputMatrix[i])
            elif keySize == 256 and i == 4:
                outputMatrix[i] = xorWords(hFunction(inputMatrix[i - 1]), inputMatrix[i])
            else:
                outputMatrix[i] = xorWords(inputMatrix[i], inputMatrix[i - 1])
            
    return outputMatrix


def computeRoundKeyList(inputMatrix, keySize, mode): # add start round
    curRKMatrix = inputMatrix
    NrOfRounds = {128 : 11, 192 : 13, 256: 15}
    rCArray = computeRoundCounterArray(NrOfRounds[keySize])
    if mode == DECRYPT:
        rCArray.reverse()
    roundKeyList = appendRoundKey([], inputMatrix)

    for i in range(NrOfRounds[keySize]):
        curRKMatrix = keyPlanRound(curRKMatrix, rCArray[i], keySize, mode)
        roundKeyList = appendRoundKey(roundKeyList, curRKMatrix)
    
    if mode == DECRYPT:
        roundKeyList.reverse()

    return roundKeyList


# HA3

inputMatrix = [[0x45,0x69,0x6e,0x66],
               [0x75,0x65,0x68,0x72],
               [0x75,0x6e,0x67,0x20],
               [0x69,0x6e,0x20,0x64],
               [0x69,0x65,0x20,0x4b],
               [0x72,0x79,0x70,0x74],
               [0x6f,0x67,0x72,0x61],
               [0x70,0x68,0x69,0x65]]

printMatrix(computeRoundKeyList(inputMatrix, 256, "encrypt"), "")




# HA2

# rCArray = computeRoundCounterArray(10)
# k1 = switchMatrixAlignment(buildMatrix(0xD09D621937BCA549A40E8AAD938B22F4, 128))
# printMatrix(keyPlanRound(k1, rCArray[0], 128, "decrypt"), "RoundKey0")

