def knapsack_packing(w, v, c):
    n = len(w)
    b = [[0 for i in range(c + 1)] for j in range(n)]
    h = [[0 for i in range(c + 1)] for j in range(n)]

    # knapsack packing algorithm
    for i in range(n):
        for j in range(c + 1):
            # old value: b[i - 1][j]
            # possible new value: b[i - 1][j - w[i]] + v[i]
            if w[i] <= j and b[i - 1][j - w[i]] + v[i] > b[i - 1][j]:
                b[i][j] = b[i - 1][j - w[i]] + v[i]
                h[i][j] = 1
            else:
                b[i][j] = b[i - 1][j]
                h[i][j] = 0
    max_v = b[n - 1][c]

    # backtrack algorithm
    p = []
    for i in range(n - 1, -1, -1):
        if h[i][c] == 1:
            p.append(i + 1)
            c -= w[i]

    # printing matrices
    print("\nknapsack matrix:\n{}".format('\n'.join([''.join(['{:3}'.format(item) 
          for item in row[1:]]) for row in b])))
    #print("\nbacktrack matrix:\n{}".format('\n'.join([''.join(['{:3}'.format(item)
    #      for item in row[1:]]) for row in h])))
    
    return (max_v, p)


def main():
    weight_list = [3,1,4,1,2,4]
    value_list = [1,2,3,2,1,1]
    capacity = 9

    max_value, stored_items = knapsack_packing(weight_list, value_list, capacity)
    print(f'\nThe maximum value is {max_value}\nto achieve that you have to pack '\
          f'the following items: {str(stored_items[::-1])[1:-1]}\n')

if __name__ == "__main__":
    main()