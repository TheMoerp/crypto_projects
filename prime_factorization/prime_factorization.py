def find_prime_factors(j):
    factors = []
    for i in range(2, (j / 2)):
        if(j % i == 0):
            
            
            return [i] + find_prime_factors(j / i)
    factors.append(j)
    return factors
