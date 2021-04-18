def primesSum2(n):
    result = list(range(n + 1))
    result[1] = 0 
    for i in result:
        if i > 1:
            for j in range(i + i, len(result), i):
                result[j] = 0
    return sum(result)

# este codigo crea un vector de 0 hasta n
# saca el 1 porque no es primo y despues lo recorre de principio a fin
#     



def primesSum2(n):
    ss = 0
    mod = 10**9 + 7
    primes = [1] * (n + 1)
    for i in range(2, n + 1):
        if primes[i] > 0:
            ss += i
            ss %= mod
            
            j = i
            while j <= n:
                primes[j] = 0
                j += i
    return ss


n=16651

print(primesSum2(16651))