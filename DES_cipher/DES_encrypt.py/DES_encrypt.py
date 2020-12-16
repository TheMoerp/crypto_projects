

KEY_STR = ""
CLEARTEXT_BIT_STR = "0000000010000000000000000000000000000000000000000000000000000000"




def inputPermutation():  # Eingangspermutation
    ipOutput = []
    ipStartNumber = [57, 51, 61, 63, 56, 58, 60, 62]
    for i in range(8):
        ipNumberCounter = ipStartNumber[i]
        for j in range(8):
            ipOutput.append(CLEARTEXT_BIT_STR[ipNumberCounter])
            ipNumberCounter -= 8
    print()
    print("Die Ausgabe der Eingangs Permutation ist:")
    print("-- " + "".join(ipOutput) + " --")
    return ipOutput


def expansion(curStr): # Expansion
    eOutput = []
    eStartNumber = 31
    for i in range(8):
        eNumberCounter = eStartNumber
        for j in range(6):
            eOutput.append(curStr[eNumberCounter])
            eNumberCounter = (eNumberCounter + 1) % 32
        eStartNumber = (eStartNumber + 4) % 32
    print()
    print("Die Ausgabe der Expansion ist:")
    eOutput = "".join(eOutput)
    print("-- " + eOutput + " --")
    return eOutput


def sBox(inputStr, sTable, sNumber):  # S-Box
    row = int(inputStr[0] + inputStr[5], 2)
    column = int(inputStr[1:5], 2)
    sBoxOutput = "{:0>4s}".format(bin(sTable[row][column])[2:])
    print()
    print("Die ausgabe von S{} ist:".format(sNumber))
    print("-- {} --".format(sBoxOutput))
    return sBoxOutput

def fPermutation(curStr):
    pTable = (15, 6, 19, 20, 28, 11, 27, 16, 0, 14, 22, 25, 4, 17, 30, 9, 1, 7, 23, 13, 31, 26, 2, 8, 18, 12, 29, 5, 21, 10, 3, 24)
    fPermutationOutput = []
    for i in range(32):
        fPermutationOutput.append(curStr[pTable[i]])
    print()
    print("Ausgabe der Permutation innerhalb der F-Funktion:")
    print("-- " + "".join(fPermutationOutput) + " --")
    return fPermutationOutput


def fFunction(curStr, curKeyStr, roundNumber):  # F-Funktion
    sTable1 = ((14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7), (0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8), (4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0), (15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13))
    sTable2 = ((15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10), (3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5), (0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15), (13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9))
    sTable3 = ((10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8), (13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1), (13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7), (1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12))
    sTable4 = ((7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15), (13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9), (10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4), (3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14))
    sTable5 = ((2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9), (14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6), (4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14), (11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3))
    sTable6 = ((12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11), (10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8), (9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6), (4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13))
    sTable7 = ((4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1), (13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6), (1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2), (6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12))
    sTable8 = ((13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7), (1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2), (7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8), (2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11))

    sBoxInputStr = bin(int(expansion("".join(curStr)), 2) ^ int(KEY_STR, 2))
    sBoxInputStr = "{:0>48}".format(sBoxInputStr[2:])
    sBoxOutput = sBox(sBoxInputStr[0:6], sTable1, 1)
    sBoxOutput += sBox(sBoxInputStr[6:12], sTable2, 2)
    sBoxOutput += sBox(sBoxInputStr[12:18], sTable3, 3)
    sBoxOutput += sBox(sBoxInputStr[18:24], sTable4, 4)
    sBoxOutput += sBox(sBoxInputStr[24:30], sTable5, 5)
    sBoxOutput += sBox(sBoxInputStr[30:36], sTable6, 6)
    sBoxOutput += sBox(sBoxInputStr[36:42], sTable7, 7)
    sBoxOutput += sBox(sBoxInputStr[42:48], sTable8, 8)
    fFunctionOutput = "".join(fPermutation(sBoxOutput))
    print()
    print("Die Ausgabe der F-Funktion ist:")
    print("-- " + fFunctionOutput + " --")
    return int(fFunctionOutput, 2)


def feistelStucture(curL, curR, curKeyStr):
    pCurR = bin(int(curL, 2) ^ fFunction(curR, curKeyStr, 1))
    curL = curR
    curL = "{:0>32s}".format(curL)
    print()
    print("Das neue L ist:")
    print("-- " + "".join(curL) + " --")
    print()
    print("Das neue R ist:")
    pCurR = "{:0>32s}".format(pCurR[2:])

    print("-- " + "".join(pCurR) + " --")
    return (curL + pCurR)
    

def feistelController():
    curIpOutput = inputPermutation()
    curIpOutput = "".join(curIpOutput)
    L = curIpOutput[0:32]
    R = curIpOutput[32:64]
    feistelStucture(L, R, KEY_STR)

feistelController()
