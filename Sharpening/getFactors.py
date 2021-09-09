
def factorSearch(n):
    from math import sqrt
    factors = []  
    for i in range(2, int(sqrt(n)) + 1):
        quotient, mod = divmod(n, i)
        if mod == 0:
            factors.append([i, quotient])
    return factors

def dfsFactors(n):
    factors = factorSearch(n)

    if len(factors) == 0:
        return []
    
    for i, factor in enumerate(factors):
        for j, value in enumerate(factor):
            subFactors = dfsFactors(value)
            for subFactor in subFactors:
                newFactor = factor[:j] + subFactor + factor[j+1:]
                factors.append(newFactor)
    return factors

def getFactors(n):
    factors = dfsFactors(n)
    result = []
    for factor in factors:
        factor.sort()
        if factor not in result:
            result.append(factor)
    
    return result

# taken from StefanPochmann's submission
def getFactorsStefanPochmann(n):
    todo, combis = [(n, 2, [])], []
    while todo:
        n, i, combi = todo.pop()
        while i * i <= n:
            if n % i == 0:
                combis += combi + [i, int(n/i)],
                todo += (n/i, i, combi+[i]),
            i += 1
    return combis

value = 32
result = getFactorsStefanPochmann(value)
print("getFactorsStefanPochmann({}):\t{}".format(value, result))