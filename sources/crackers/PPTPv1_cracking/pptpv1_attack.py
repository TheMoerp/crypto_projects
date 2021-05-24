#!/usr/bin/python

import hashlib
import sys
import time



def getUpLetter(number):
	return str(unichr(ord('A')+number))

def getHexByteStr(number):
	return "%02x" % number

def md5(password, constant):
	m = hashlib.md5()
	m.update(str.encode(password + constant))
	return m.hexdigest()

def lmh(password, constant):
	while len(password) <= 14:
		password = password + "0"
	password = password.upper()
	return md5(password[:7], constant)[:16] + md5(password[7:14], constant)[:16]

def wnth(password, constant):
	while len(password) <= 14:
		password = password + "0"
	return md5(password, constant)[:32]

def chap(password, constant, challenge):
	firstHash = lmh(password, constant) + "0000000000"
	secondHash = wnth(password, constant) + "0000000000"
	res1 = md5(firstHash[:14],challenge)[:16]
	res2 = md5(firstHash[14:28],challenge)[:16]
	res3 = md5(firstHash[28:42],challenge)[:16]
	res4 = md5(secondHash[:14],challenge)[:16]
	res5 = md5(secondHash[14:28],challenge)[:16]
	res6 = md5(secondHash[28:42],challenge)[:16]
	return res1 + res2 + res3 + res4 + res5 + res6


const = "NetSec1"
chall = "GoodLuck!"
resp = "0bc770ca8473d2e659fd6683dae3a1b3c60ffab3c0c2a610ac4c1341d6633f040379a12d15531b73c4751c98268eb4b3" # change resp to resp of pwd



################ ATTACK ################


SMALL_WORDLIST_PATH = "small2_wordlist.txt" # chose the right on. lenght shout be equel to password length - 7. In uppercase
TWO_CHAR_WORDLIST_PATH = "2char_wordlist.txt" # 2 char long abc+0-9 in lowercase
BIG_WORDLIST_PATH = "big_wordlist.txt" # 6 char long abc in uppercase

PASSWORD_LENGTH = 9
FIRST_LETTER = "Y" # has to be uppercase


def ConvertStringToList(str):
    list = []
    list[:0] = str
    return list


def ReadInGenerator(filePath):
	with open(filePath, "r") as f:
		while True:
			curLine = f.readline()

			if(curLine == ''):
				break
			curLine = curLine.strip('\n')
			curLine = curLine.strip('\r')
			yield(curLine)


def PPTPv1Attack():
	print("Starting PPTPv1 Attack...\nKnown letters: {}\nPassword length: {}\n\n#----------------------------------------------------#".format(FIRST_LETTER, PASSWORD_LENGTH))
	t0 = time.time()

	# compute right password part

	rightPwdGen = ReadInGenerator(SMALL_WORDLIST_PATH)
	rPwdOptList = []
	while True:
		try:
			curLine = next(rightPwdGen)
		except StopIteration:
			if(len(rPwdOptList) == 0):
				print("No matching Password has been found.")
				return "Error!!!"
			else:
				break

		curRightPwd = "{:0<7}".format(curLine)
		rightLmhOut = "{:0<26}".format(md5(curRightPwd, const)[:16])

		resp3Cand = md5(rightLmhOut[12:26], chall)[:16]
		if(resp3Cand == resp[32:48]):
			rPwdOptList.append((curRightPwd, rightLmhOut))

	missingCharGen = ReadInGenerator(TWO_CHAR_WORDLIST_PATH)
	correctPwdChar = ""
	for curRPwdOpt in rPwdOptList:
		while True:
			try:
				charCand = next(missingCharGen)
			except StopIteration:
				print("\nNo matching chars has been found.")
				return "Error!!!"

			rightLmhOut = curRPwdOpt[1]
			middleMd5In = "{}{}".format(charCand, rightLmhOut[:12])

			resp2Cand = md5(middleMd5In, chall)[:16]
			if(resp2Cand == resp[16:32]):
				correctPwdChar = (curRPwdOpt[0], charCand)
				print("Right password half has been found.")
				break
	
	# compute left password part

	leftPwdGen = ReadInGenerator(BIG_WORDLIST_PATH)
	correctPwd = ""
	while True:
		try:
			curLine = next(leftPwdGen)
		except StopIteration:
			print("\nNo matching Password has been found.")
			return "Error!!!"

		curLeftPwd = "{}{}".format(FIRST_LETTER, curLine)

		leftLmhOut = md5(curLeftPwd, const)[:16]
		if(leftLmhOut[14:] == correctPwdChar[1]):
			resp1Cand = md5(leftLmhOut[:14], chall)[:16]
			if(resp1Cand == resp[:16]):
				correctPwd = curLeftPwd + correctPwdChar[0][:PASSWORD_LENGTH - 7]
				print("Left password half has been found.\nFull password has been found.")
				break

	# Compute the char cases

	for i in range(2 ** len (correctPwd)):
		correctPwd = ConvertStringToList(correctPwd)
		for j in range(len(correctPwd)):
			mask = 1
			if(j > 0):
				mask = 0x01<<(j)
			if ((i & mask) != 0):
				correctPwd[j] = correctPwd[j].upper()
			else:
				correctPwd[j] = correctPwd[j].lower()
		correctPwd = "".join(correctPwd)

		wnthOut = wnth(correctPwd, const) + "0000000000"
		resp4Cand = md5(wnthOut[:14], chall)[:16]
		if(resp4Cand != resp[48:64]):
			continue
		resp5Cand = md5(wnthOut[14:28], chall)[:16]
		if(resp5Cand != resp[64:80]):
			continue
		resp6Cand = md5(wnthOut[28:42], chall)[:16]
		if(resp6Cand != resp[80:96]):
			continue

		t1 = time.time()
		compTime = int(t1 - t0)
		print("Upper and lower case of the password has been found.\n\nThe correct password is: {}\nComputing time: {}s\n#----------------------------------------------------#\n".format(correctPwd, compTime))
		return (correctPwd)


PPTPv1Attack()



