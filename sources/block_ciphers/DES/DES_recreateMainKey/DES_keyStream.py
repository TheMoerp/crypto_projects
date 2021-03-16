KEY_ROUND1 = "{:0>48b}".format(0xD4073813ACE0)
KEY_ROUND2 = "{:0>48b}".format(0x32C9E25072DF)
BYTE_LENGTH = 8


def inversePC2 (curKey):
    invPC2Tbl = [4, 23, 6, 15, 5, 9, 19, 17, "U", 11, 2, 14, 22, 0, 8, 18, 1, "U",
                 13, 21, 10, "U", 12, 3, "U", 16, 20, 7, 46, 30, 26, 47, 34, 40, "U",
                 45, 27, "U", 38, 31, 24, 43, "U", 36, 33, 42, 28, 35, 37, 44, 32, 25,
                 41, "U", 29, 39]
    invPC2Output = []

    for PC2Value in invPC2Tbl:
        if PC2Value != "U":
            invPC2Output.append(curKey[PC2Value])
        else:
            invPC2Output.append("0")
    
    invPC2Output = int("".join(invPC2Output), 2) 
    return invPC2Output


def rightShift (rightShiftInput):
    print(rightShiftInput);
    copyMask = 0b0000000000000000000000000001
    copyedBit = (rightShiftInput & copyMask) << 29
    rightShiftInput = rightShiftInput | copyedBit
    rightShiftOutput = rightShiftInput >> 1
    return rightShiftOutput


def copyUnknownBits (invTransOutput):
    unknownMask = 0b00000000010000000010001001000000000100100001000000000010
    copyedUnknownBits = invTransOutput & unknownMask
    return copyedUnknownBits


def slicer (slicerInput):
    mask = 0b1111111111111111111111111111
    rightPart = slicerInput & mask
    leftPart = slicerInput >> 28
    return (leftPart, rightPart)


def reversedSlicer (leftPart, rightPart):
    reversedSlice = leftPart << 28 | rightPart
    return (reversedSlice)


def shiftingFunction (shiftingInput):
    slicerOutput = slicer(shiftingInput)
    shiftingOutput = reversedSlicer(rightShift(slicerOutput[0]), rightShift(slicerOutput[1]))
    return shiftingOutput


def inverseTransformation (curRoundKey):
    invTransOutput = shiftingFunction(inversePC2(curRoundKey))

    return invTransOutput


def inversePC1 (invPC1Input):
    invPC1Tbl = [7, 15, 23, 55, 51, 43, 35, "U", 6, 14, 22, 54, 50, 42, 34, "U", 5, 13, 21, 53, 49,
                 41, 33, "U", 4, 12, 20, 52, 48, 40, 32, "U", 3, 11, 19, 27, 47, 39, 31, "U", 2, 10,
                 18, 26, 46, 38, 30, "U", 1, 9, 17, 25, 45, 37, 29, "U", 0, 8, 16, 24, 44, 36, 28, "U"]
    invPC1Output = []
    invPC1Input = "{:0>56b}".format(invPC1Input)
    for PC1Value in invPC1Tbl:
        if PC1Value != "U":
            invPC1Output.append(invPC1Input[PC1Value])
        else:
            invPC1Output.append("0")

    invPC1Output = "".join(invPC1Output)
    return invPC1Output


def getEffictivMainKey ():
    invOutputPC21 = inversePC2(KEY_ROUND1)
    transOutputKey2 = inverseTransformation(KEY_ROUND2)
    effectivKey = copyUnknownBits(invOutputPC21) | transOutputKey2
    effectivKey = shiftingFunction(effectivKey)
    return effectivKey


def computeCompleteKey ():
    compKey = inversePC1(getEffictivMainKey())
    print("\nDer Hauptschlüssel als Binärzahl: 0b{}\nDer Hauptschlüssel als Hexa-Dezimalzahl: 0x{}\n"
          .format(compKey, hex(int(compKey, 2))[2:].upper()))


computeCompleteKey()