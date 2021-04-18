#   devolver el mayor producto de dos números que esten juntos en el array

def adjacentElementsProduct(inputArray):
    
    aux=inputArray[0]*inputArray[1]
    for i in range(2,len(inputArray)):
        if (inputArray[i-1]*inputArray[i])>aux:
            aux=(inputArray[i-1]*inputArray[i])
    
    return(aux)


def adjacentElementsProduct2(inputArray):
    return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])


def adjacentElementsProduct3(inputArray):
    return max(a * b for a, b in zip(inputArray[:-1], inputArray[1:]))



A=[3, 6, -2, -5, 7, 3, 1, 9, 7, -2, 4, -6, 2, 8, 9, 9, 2, 2, 3, 5, 1, 9, 8, 8, -8, 7, -9, 4, -4, -1, 4, 2, 5, -6, 7, 8, 1, 4, 7]


print(A[:-1])   #del principio al fin -1
print(A[1:])    #desde posición 1 hasta fin
print(A[::-1])  #invierte la variable
print(A[-3:])   #los ultimos 3 elementos

print(adjacentElementsProduct(A))

