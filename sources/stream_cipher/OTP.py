

cleartext_start = 'https://'
ciphertext_hex = '4e 7e 1d d1 fa 8c f6 8a d7 d5 f5 8c 36 e5 9b 76 21 47 47 8a 94 de 7e d0 74 f4 49 27'

ciphertext_hex_list = ciphertext_hex.split(' ')
ciphertext = list(map(lambda x: int(x, 16), ciphertext_hex_list))
# print(ciphertext)


# key computation
s = []
s.append(ord(cleartext_start[0]) ^ ciphertext[0])
s.append(ord(cleartext_start[1]) ^ ciphertext[1])

a = 83
b = 197
c = 13
m = 257

for i in range(1, 27):
    sip1 = (a * s[i] + b * s[i-1] + c) % m
    s.append(sip1)

# print(s)


cleartext = []
for (c,k) in zip(ciphertext, s):
    cleartext.append(c ^ k)

#print(cleartext)

cleartext_str = ''.join(map(chr, cleartext))
print(cleartext_str)


