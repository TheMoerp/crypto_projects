def knapsack_packing(n, w, v, c):
    # knapsack packing algorithm
    b = [[0 for i in range(c + 1)] for j in range(n)]
    h = [[0 for i in range(c + 1)] for j in range(n)]

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
    print("\nbacktrack matrix:\n{}".format('\n'.join([''.join(['{:3}'.format(item)
          for item in row[1:]]) for row in h])))
    
    return (max_v, p)



def main():
    item_amount = 6
    weight_list = [4,6,2,1,3,5]
    value_list = [6,3,5,1,4,2]
    capacity = 9

    max_value, stored_items = knapsack_packing(item_amount, weight_list,
                                               value_list, capacity)
    print(f'\nThe maximum value is {max_value}\nto achieve that you have to pack '\
          f'the following items: {str(stored_items[::-1])[1:-1]}\n')

if __name__ == "__main__":
    main()