#!/usr/bin/python

import hashlib
import sys


def md5(pwd, const):
    m = hashlib.md5()
    m.update(str.encode(pwd + const))
    return m.hexdigest()



#--------------------------------------------------------------#

HASH = "f4a62fe37d95bbe4711443480ffa5306"
MAX_PWD_LENGTH = 9

def computePassword(hash):
    leftHashCheck = HASH[:16]
    rightHashCheck = HASH[16:]

    print("LeftHashCheck: {}".format(leftHashCheck))
    print("RightHashCheck: {}".format(rightHashCheck))
    print("Searching for a password with {} characters...".format(MAX_PWD_LENGTH))
    print("")

    leftPwd = ""
    rightPwd = ""

    foundLeft = False
    foundRight = False
    while True:
        rtPwd = sys.stdin.readline()

        if rtPwd == '':
            print("#------------------------------------------------#")
            return "The password is not in the wordlist."

        rtPwd = rtPwd.strip('\n')
        rtPwd = rtPwd.strip('\r')

        hashedRtPwd = md5(rtPwd, "NetSec1")

        if hashedRtPwd[:16] == leftHashCheck:
            foundLeft = True
            leftPwd = rtPwd
            print("Left half of the password: {}".format(rtPwd))
        elif hashedRtPwd[0:16] == rightHashCheck:
            foundRight = True
            rightPwd = rtPwd
            print("Right half of the password: {}".format(rtPwd))

        if foundRight and foundLeft:
            print("#------------------------------------------------#")
            return leftPwd + rightPwd
            

print("The matching Password is: {}".format(computePassword(HASH)[:MAX_PWD_LENGTH]))

    
