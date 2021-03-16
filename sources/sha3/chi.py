def chi_step(state):
    xLen = len(state)
    yLen = len(state[0])
    for x in range(xLen):
        for y in range(yLen):
            state[x][y] ^= (state[(x + 1) % xLen][y] ^ 0b1111) & state[(x + 2) % xLen][y]  
    return state


def print_state(state):
    xLen = len(state)
    yLen = len(state[0])
    for x in range(xLen): 
        print("Sheet x = {}".format(x))
        for y in range(yLen):
            outputLine = "{:0>4s}".format(bin(state[x][y])[2:])
            for curBit in outputLine:
                print("{}  ".format(curBit), end='')
            print("")
        print("")


state = [[0b0111, 0b0101, 0b1110, 0b0000, 0b0001],
         [0b0001, 0b1010, 0b0101, 0b1001, 0b1101],
         [0b0010, 0b0101, 0b0111, 0b0101, 0b1010],
         [0b1010, 0b0101, 0b0010, 0b0101, 0b1100],
         [0b0111, 0b1110, 0b1100, 0b0111, 0b0010]]


print_state(chi_step(state))
