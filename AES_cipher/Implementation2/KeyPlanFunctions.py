from shiftRow import shiftingFunction
from substitutionLayer import sBox
from constants import ENCRYPT


def gFunction(inputWord, curRC):
    outputWord = sBox([shiftingFunction(inputWord, 3)], ENCRYPT)[0]
    outputWord[0] ^= curRC
    return outputWord


def hFunction(inputWord):
    outputWord = sBox([inputWord], ENCRYPT)[0]
    return outputWord