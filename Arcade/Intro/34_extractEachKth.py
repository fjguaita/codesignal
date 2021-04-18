# Given array of integers, remove each kth element from it.

# output será inputArray sin los elementos k - 1, 2k - 1, 3k - 1 etc.

def extractEachKth(a, k):
    kth = list(range(k-1,len(a),k))
    return [a[i] for i in range(len(a)) if i not in kth] 


a= [2, 4, 6, 8, 10]
k= 2                    # salida [2, 6, 10]

a2= [1, 2, 1, 2, 1, 2, 1, 2]
k2= 2                   # salida [1, 1, 1, 1]



# la otra mas simple que encontramos siempre

def extractEachKth2(inputArray, k):
    del inputArray[k-1::k]
    return inputArray



print(extractEachKth(a2, k2))
print(extractEachKth2(a2, k2))
