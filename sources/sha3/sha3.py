rotTable = [[25, 55, 28, 56, 21],
            [39, 20, 27, 14, 8],
            [3, 36, 0, 18, 41],
            [10, 44, 1, 2, 45],
            [43, 6, 62, 61, 15]]


def theta_step(state, xLen, yLen, zLen):
    newState = [[[0 for z in range(zLen)] for y in range(yLen)] for x in range(xLen)]
    for x in range(xLen):
        for y in range(yLen):
            for z in range(zLen):
                curBit = state[x][y][z]
                for i in range(yLen):
                    curBit ^= state[(x + 1) % xLen][i][(z - 1) % zLen]
                    curBit ^= state[(x - 1) % xLen][i][z]
                newState[x][y][z] = curBit
    return newState


# def rho_step(state, xLen, yLen, zLen):
#     newState = [[[0 for z in range(zLen)] for y in range(yLen)] for x in range(xLen)]
    




# def chi_step(state, xLen, yLen, zLen):
#     newState = [[[0 for z in range(zLen)] for y in range(yLen)] for x in range(xLen)]
#     for x in range(xLen):
#         for y in range(yLen):
#             for z in range(zLen):
#                 curBit = state[x][y][z]
#                 curBit ^= (state[(x + 1) % xLen][y][z] ^ 0b1) & state[(x + 2) % xLen][y][z]
#             newState[x][y][z] = curBit
#     return newState






def print_state(state, xLen, yLen, zLen):
    for x in range(xLen): 
        print("Sheet x = {}".format(x))
        for y in range(yLen - 1, -1, -1):
            for z in range(zLen):
                print("{}  ".format(state[x][y][z]), end='')
            print("")
        print("")






xLen = 5
yLen = 5
zLen = 4

state = [[[0,0,0,1],
          [0,0,0,0],
          [1,1,1,0],
          [0,1,0,1],
          [0,1,1,1]], # x0
         [[1,1,0,1],
          [1,0,0,1],
          [0,1,0,1],
          [1,0,1,0],
          [0,0,0,1]], # x1
         [[1,0,1,0],
          [0,1,0,1],
          [0,1,1,1],
          [0,1,0,1],
          [0,0,1,0]], # x2
         [[1,1,0,0],
          [0,1,0,1],
          [0,0,1,0],
          [0,1,0,1],
          [1,0,1,0]], # x3
         [[0,0,1,0],
          [0,1,1,1],
          [1,1,0,0],
          [1,1,1,0],
          [0,1,1,1]]] # x3


print_state(chi_step(state, xLen, yLen, zLen), xLen, yLen, zLen)