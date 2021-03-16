import ecc_operations as ecc


def double_add(start_point, factor, a, p):
    print('{:-^40}\nDouble-and-Add: {}{}:\n'.format('Double-and-Add',
          factor, start_point))
    tmp_point = start_point
    for i in bin(factor)[3:]:
        if i == '1':
            tmp_point = ecc.point_doubling(tmp_point, a, p)
            tmp_point = ecc.point_addition(tmp_point, start_point, p)
            print(f'{tmp_point} Double-and-Add')
        else:
            tmp_point = ecc.point_doubling(tmp_point, a, p)
            print(f'{tmp_point} Double')
    print(f'\nresult: {tmp_point}\n{40*"-"}')
    return tmp_point


def main():
    slice_point = lambda x : (int(x[0][1:]), int(x[1][:-1]))
    start_point = slice_point(input('point to start eg.: (3,5): ').split(','))
    factor = int(input('factor: '))
    a = int(input('a: '))
    p = int(input('p: '))
    double_add(start_point, factor, a, p)

if __name__ == "__main__":
    main()