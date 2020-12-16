IRREDUCIBLE_POL = [1, 0, 0, 0, 1, 1, 0, 1, 1]
IRREDUCIBLE_POL_LENGTH = len(IRREDUCIBLE_POL)
IRREDUCIBLE_POL.reverse() 



def numberToPolynom(inputNr):
    outputList =[]
    outputList = [int(curBit) for curBit in bin(inputNr)[2:]]
    outputList.reverse()

    return outputList


def polynomToNumber(inputPol):
    inputPol.reverse()
    outputNr = int("".join(str(curBit) for curBit in inputPol), 2)
    
    return outputNr


def preMultiplication(inputPol1, inputPol2):
    outputPol = [0] * (len(inputPol1) + len(inputPol2))

    for i in range(len(inputPol1)):
        for j in range(len(inputPol2)):
            outputPol[i + j] ^= (inputPol1[i] & inputPol2[j])

    return outputPol


def polynomDevisionStep(inputPol):
    inputPolLength = len(inputPol)
    outputPol = [0] * (inputPolLength)
    biggestExp = 0

    for i in range(inputPolLength - 1, 0, -1):
        if inputPol[i] == 1:
            biggestExp = i
            break
        else:
            biggestExp = 0

    curResult = biggestExp - (IRREDUCIBLE_POL_LENGTH - 1)
    if curResult >= 1 or curResult == 0:
        for i in range(IRREDUCIBLE_POL_LENGTH):
            outputPol[i + curResult] = IRREDUCIBLE_POL[i]
        for i in range(inputPolLength):
            outputPol[i] ^= inputPol[i]

        return (outputPol, True)
    else:
        return (inputPol, False)


def polynomDevision(inputPol):
    runPolDev = True
    for i in range(len(inputPol) - 1):
        if runPolDev:
            inputPol, runPolDev = polynomDevisionStep(inputPol)
        else:
            break
    
    outputNr = polynomToNumber(inputPol)
    return outputNr


def multiplicationGF(fac1, fac2):
    return polynomDevision(preMultiplication(numberToPolynom(fac1), numberToPolynom(fac2)))


def equalizeSize(inputList, goalLength):
    while(len(inputList) != goalLength):
        inputList.append(0)

    return inputList


def additionGF(sumd1, sumd2):
    sumd1 = numberToPolynom(sumd1)
    sumd2 = numberToPolynom(sumd2)
    sumOutputLength = len(sumd1) if len(sumd1) >= len(sumd2) else len(sumd2)
    sumd1 = equalizeSize(sumd1, sumOutputLength)
    sumd2 = equalizeSize(sumd2, sumOutputLength)
    
    for i in range(sumOutputLength):
        sumd1[i] ^= sumd2[i]

    sumOutput = polynomToNumber(sumd1)
    return sumOutput

nr1 = 63
nr2 = 32

print(preMultiplication(numberToPolynom(nr1), numberToPolynom(nr2)))


# nr1 = 0b10100110
# nr2 = 0b1101

# print("\nAddition in GF(2^8):\n0b{:0>8b} + 0b{:0>8b} = 0b{:0>8b}\n0x{} * 0x{} = 0x{}\n".format(nr1, nr2, additionGF(nr1, nr2), hex(nr1)[2:].upper(), hex(nr2)[2:].upper(), hex(additionGF(nr1, nr2))[2:].upper()))

print("\nMultiplication in GF(2^8):\n0b{:0>8b} * 0b{:0>8b} = 0b{:0>8b}\n0x{} * 0x{} = 0x{}\n".format(nr1, nr2, multiplicationGF(nr1, nr2), hex(nr1)[2:].upper(), hex(nr2)[2:].upper(), hex(multiplicationGF(nr1, nr2))[2:].upper()))

