CLEARTEXT_1 =  "{:0>64b}".format(0xE54DEDBF2E8A749D)
CLEARTEXT_2 =  "{:0>64b}".format(0xC38F7976D1658A42)
CIPHERTEXT_1 = "{:0>64b}".format(0x2E8A749D26049F39)
CIPHERTEXT_2 = "{:0>64b}".format(0xD1658A428FA5CE40)
HALF_TEXT_LENGTH = 32
INV_SBOX_OUTPUT_LENGTH = 6
INV_SBOX_INPUT_LENGTH = 4
BYTE_LENGTH = 8


def splitInputtext(inputStr):
    splitedInputStr = []
    slicer = 0
    for i in range(2):
        splitedInputStr.append(inputStr[slicer : slicer + HALF_TEXT_LENGTH])
        slicer += HALF_TEXT_LENGTH

    return splitedInputStr


def inverseSBox(invSBoxInput, curSTbl):
    sBoxOutputList = []
    invSBoxInput = int(invSBoxInput, 2)
    for i in range(len(curSTbl)):
        for j in range(len(curSTbl[0])):
            if(curSTbl[i][j] == invSBoxInput):
                curRow = "{:0>2b}".format(i)
                curColumn = "{:0>4b}".format(j)
                sBoxOutputList.append("{}{}{}".format(curRow[0], curColumn, curRow[1]))

    return sBoxOutputList


def getCompleteSBoxOutput(invSBoxInputStr):
    sTblList = (((14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7), (0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8), (4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0), (15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13)),
            ((15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10), (3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5), (0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15), (13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9)),
            ((10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8), (13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1), (13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7), (1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12)),
            ((7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15), (13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9), (10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4), (3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14)),
            ((2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9), (14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6), (4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14), (11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3)),
            ((12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11), (10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8), (9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6), (4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13)),
            ((4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1), (13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6), (1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2), (6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12)),
            ((13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7), (1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2), (7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8), (2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11)))
    CompleteSBoxOutputList = []
    slicer = 0
    for sTbl in sTblList:
        CompleteSBoxOutputList.append(inverseSBox(invSBoxInputStr[slicer : slicer + INV_SBOX_INPUT_LENGTH], sTbl))
        slicer += INV_SBOX_INPUT_LENGTH
    return CompleteSBoxOutputList


def expansion(expansionsInput):
    expansionsInputLenth = len(expansionsInput)
    expansionsOutput = []
    expansionsStartNr = expansionsInputLenth - 1
    for i in range(BYTE_LENGTH):
        expansionsNrCnt = expansionsStartNr
        for j in range(INV_SBOX_OUTPUT_LENGTH):
            expansionsOutput.append(expansionsInput[expansionsNrCnt])
            expansionsNrCnt = (expansionsNrCnt + 1) % expansionsInputLenth
        expansionsStartNr = (expansionsStartNr + INV_SBOX_INPUT_LENGTH) % expansionsInputLenth

    expansionsOutput = "".join(expansionsOutput)
    return expansionsOutput


def inversePermutation(invPermutationsInput): 
    invPermutationsTbl = (8, 16, 22, 30, 12, 27, 1, 17, 23, 15, 29, 5, 25, 19, 9, 0, 7,
                          13, 24, 2, 3, 28, 10, 18, 31, 11, 21, 6, 4, 26, 14, 20)
    invPermutationsOutput = []
    for permutationsValue in invPermutationsTbl: 
        invPermutationsOutput.append(invPermutationsInput[permutationsValue])
    invPermutationsOutput = "".join(invPermutationsOutput)
    return invPermutationsOutput


def createPossibleKeyPartList(invSBoxOutputList, expansionsOutput):
    KeyPartList = []
    slicer = 0
    for i in range(BYTE_LENGTH):
        KeyPartListSeq = []
        for j in range(INV_SBOX_INPUT_LENGTH):
            keyPart = "{:0>6b}".format(int(invSBoxOutputList[i][j], 2) ^ int(expansionsOutput[slicer : slicer + INV_SBOX_OUTPUT_LENGTH], 2))
            KeyPartListSeq.append(keyPart)
        KeyPartList.append(KeyPartListSeq)
        slicer += INV_SBOX_OUTPUT_LENGTH

    return KeyPartList


def compareKeyPartList(keyPartList1, keyPartList2):
    for KeyPart1 in keyPartList1:
        if KeyPart1 in keyPartList2:
            return KeyPart1


def prepKeyList(curCleartext, curCiphertext):
    splitedCleartext = splitInputtext(curCleartext)
    splitedCiphertext = splitInputtext(curCiphertext)
    invPermutationInput = "{:0>32b}".format(int(splitedCleartext[0], 2) ^ int(splitedCiphertext[1], 2))
    possibleKeyPartList = createPossibleKeyPartList(getCompleteSBoxOutput(inversePermutation(invPermutationInput)), expansion(splitedCleartext[1]))
    return possibleKeyPartList


def getcorrectKey():
    prepedKeyList1 = prepKeyList(CLEARTEXT_1, CIPHERTEXT_1)
    prepedKeyList2 = prepKeyList(CLEARTEXT_2, CIPHERTEXT_2)
    correctKeyPartList = []
    for i in range(BYTE_LENGTH):
        correctKeyPartList.append(compareKeyPartList(prepedKeyList1[i], prepedKeyList2[i]))
        correctKey = "".join(correctKeyPartList)
    print("\nDer Rundenschlüssel als Binärzahl: 0b{}\nDer Rundenschlüssel als Hexa-Dezimalzahl: 0x{}\n".format(correctKey, hex(int(correctKey, 2))[2:].upper()))
    

getcorrectKey()