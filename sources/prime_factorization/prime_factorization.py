def find_prime_factors(num):
    factors = []
    for i in range(2, (num // 2)):
        if(num % i == 0):
            return [i] + find_prime_factors(num // i)
    factors.append(num)
    return factors


def main():
    num = int(input('Find prime factors of: '))
    print(find_prime_factors(num))

if __name__ = "__main__":
    main()