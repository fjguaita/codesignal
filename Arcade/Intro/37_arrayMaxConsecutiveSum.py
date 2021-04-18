# Given array of integers, find the maximal possible sum of some of its k consecutive elements.

def arrayMaxConsecutiveSum(a, k):

    return max([sum(a[i:i+k]) for i in range(len(a)-k+1)])
 
    

a= [2, 3, 5, 1, 6]
k= 2                # salida -> 8  

a2= [1, 3, 2, 4]
k2= 3                # salida -> 9  

a3= [1, 3, 2, 4]
k3= 3               # salida  -> 9

print(arrayMaxConsecutiveSum(a3,k3))

# funciona pero se pasa de timepo en el ultimo




def arrayMaxConsecutiveSum2(a, k):
    s = m = sum(a[:k])                  # arranca con la suma de los primeros k numeros
    for i in range(k, len(a)):
        s += a[i] - a[i-k]              # en cada movimiento le suma el ultimo numero y resta el primero
        if s > m: m = s                 # compara y se queda con el mayor
    return m


a3= [1, 3, 2, 4]
k3= 3   

print(arrayMaxConsecutiveSum2(a3,k3))