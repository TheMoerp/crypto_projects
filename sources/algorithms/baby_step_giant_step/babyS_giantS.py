from math import ceil, sqrt
from eea import eea

def babystep_giantstep(alpha, beta, g):
    m = ceil(sqrt(g - 1))
    giant_alpha = eea(g, (alpha ** m) % g)
    babystep_list = list(map(lambda x : (alpha ** x) % g, range(m)))
    giantstep_list = list(map(lambda x : ((giant_alpha ** x) * beta) % g, range(m)))

    for i in range(len(babystep_list)):
        for j in range(len(giantstep_list)):
            if babystep_list[i] == giantstep_list[j]:
                x_b = i
                x_g = j
                x = x_g * m + x_b
                print(f'x: {x_g} * {m} + {x_b} = {x}') 


def main():
    alpha = int(input('alpha: '))
    beta = int(input('beta: '))
    g = int(input('g (Prim): '))
    babystep_giantstep(alpha, beta, g)

if __name__ == "__main__":
    main()