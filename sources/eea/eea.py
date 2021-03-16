def eea(mod, num):
    print(f'{40*"-"}\neea({mod},{num})\n')
    r = [mod, num]
    t = [0, 1]
    q = [0]
    i = 1
    print(f'Round {i}: r0 = {r[0]}, r1 = {r[1]}, t0 = {t[0]}, '\
          f't1 = {t[1]}, q0 = {q[0]}')
    while True:
        i += 1
        r.append(r[i - 2] % r[i - 1])
        q.append(int((r[i - 2] - r[i]) / r[i - 1]))
        t.append(t[i - 2] - q[i - 1] * t[i - 1])
        print(f'Round {i}: r{i} = {r[i]}, t{i} = {t[i]}, q{i-1} = {q[i-1]}')

        if r[i] == 0:
            break
    invNum = t[i - 1]
    while invNum < 0:
        invNum = invNum + mod
    print(f'\n{num}^-1 mod {mod} = {invNum}\n{40*"-"}')
    return invNum


def main():
    import re
    input_eea = input('Enter the paramter eg.: eea(25,4): ')
    regex = re.compile(r'eea\((\d+),(\d+)\)')
    match = regex.match(input_eea)
    eea(int(match[1]), int(match[2]))

if __name__ == "__main__":
    main()