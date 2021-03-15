# doesnt work everytime with find_prime_factors()
def find_prime_factors(j):
    factors = []
    for i in range(2, (j // 2)):
        if(j % i == 0):
            return [i] + find_prime_factors(j // i)
    factors.append(j)
    return factors

def element_amount(group_num):
    pos_cardinality = find_prime_factors(group_num-1)
    pos_cardinality.append(group_num-1)
    pos_cardinality.insert(0, 1)
    cardinality_cnt = {}
    for i in range(1, group_num):
        for j in pos_cardinality:
            if (i**j)%group_num == 1:
                try:
                    if cardinality_cnt[j] >= 1:
                        cardinality_cnt[j] += 1       
                except:
                    cardinality_cnt[j] = 1
                break
    return cardinality_cnt