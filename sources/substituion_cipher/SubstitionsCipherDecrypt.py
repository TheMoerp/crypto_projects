import sys

shiftedChars = {
    'A':'E',
    'B':'U',
    'C':'F',
    'D':'H',
    'E':'W',
    'F':'R',
    'G':'K',
    'H':'S',
    'I':'M',
    'J':'Z',
    'K':'J',
    'L':'B',
    'M':'Y',
    'N':'P',
    'O':'D',
    'P':'N',
    'Q':'A',
    'R':'I',
    'S':'V',
    'T':'X',
    'U':'G',
    'V':'T',
    'W':'C',
    'X':'Q',
    'Y':'L',
    'Z':'O'}    #Substitutionstabelle


if len(sys.argv) == 2:  #Chiffrat einfügen
    src = sys.argv[1]
else:   #falls kein Chiffrat eingefügt wurde, aufforden etwas einzufügen
    print("Füge einen Verschlüsselten Text hinzu!")
    exit()

with open(src, "r") as f:   #Chiffrat zum lesen öffnen
    text = f.read()
    clearText = []  
    for cryptedChar in text:
        if cryptedChar in shiftedChars:     #ist das Zeichen in der Substitutionstabelle?
            clearChar = shiftedChars[cryptedChar]   #Buchstaben ersetzen
            clearText.append(clearChar)     #entschlüsselten Buchstaben zum Klartext hinzufügen
        else:
            clearText.append(cryptedChar)   #nicht in Substitutionstabelle verhandenes Zeichen unverändert übernehmen

print("".join(clearText))   #Klartext ausgeben


