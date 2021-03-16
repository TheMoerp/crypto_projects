def ggt(num1, num2):
    r = [num1, num2]
    i = 1
    while True: 
        i += 1
        r.append(r[i-2] % r[i-1])
        print(r)
        if r[i] == 0:
            break
    return r[i - 1]


def main():
    import re
    input_ggt = input('Enter the paramter eg.: ggt(25,4): ')
    regex = re.compile(r'ggt\((\d+),(\d+)\)')
    match = regex.match(input_ggt)
    print(ggt(int(match[1]), int(match[2])))

if __name__ == "__main__":
    main()