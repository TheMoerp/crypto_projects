BYTE_LENGTH = 8
FEEDBACK_COEFFICIENT = [0,1,1,0,0,1,0,1]  # Rückkopplungskoeffizienten
flipflopStorage = [1,0,1,1,1,1,0,0]  # Startspeicherwerte
CIPHER_TEXT = [0x78, 0x55, 0x49, 0x32, 0xFB, 0xC6, 0x55, 0x7B, 0xB4, 0x1F, 0x40, 0x5F, 0xAA, 0xC8]  # Verschlüsslter Text
clearText = []


def nextKey():  # Schlüsselbyte erzeugen
    for i in range(BYTE_LENGTH):

        newKey = 0
        for j in range(BYTE_LENGTH):  # neues Schlüsselbit erzeugen
            newKey ^= (flipflopStorage[j] * FEEDBACK_COEFFICIENT[j])
    
        for k in range(BYTE_LENGTH):
            if(k != BYTE_LENGTH - 1):  # Inhalt des LFSR verschieben
                flipflopStorage[BYTE_LENGTH - 1 - k] = flipflopStorage[BYTE_LENGTH - 2 - k]
            else :
                flipflopStorage[0] = newKey  # neues Schlüsselbit anhängen

    return flipflopStorage # Schlüsselbyte ausgeben


for i in range(len(CIPHER_TEXT)):  # so viele Schlüsselbytes erzeugen wie der Verschlüsselte Text lang ist

    if(i > 0):
        keyByteList = nextKey()
    else:
        keyByteList = flipflopStorage
    
    keyByte = 0
    for j in range(BYTE_LENGTH) :  # Wert der Schlüsselbyteliste berechnen
        keyByte += keyByteList[j] * 2 ** j

    clearText.append(chr(CIPHER_TEXT[i] ^ keyByte))  # Klartext Byte mit Schlüssel Byte entschlüsseln


print("Der Klartext ist: ","".join(clearText))  # Klartext ausgeben






    
