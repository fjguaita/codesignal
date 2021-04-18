import numpy as np
def absoluteValuesSumMinimization(a):
    a=np.array(a)
    b=[sum(abs(a-i)) for i in a]
    return a[b.index(min(b))]




# esto si no entiendo xq funciona
def absoluteValuesSumMinimization2(a):
    return a[len(a)-1//2]



a1= [1, 1, 3, 4]     #1
a2= [-1000000, -10000, -10000, -1000, -100, -10, -1, 0, 1, 10, 100, 1000, 10000, 100000, 1000000]       #0



print(absoluteValuesSumMinimization(a1))
print(absoluteValuesSumMinimization(a2))



#   Given a sorted array of integers a, your task is to determine which element of a is closest 
#  to all other values of a. In other words, find the element x in a, which minimizes the following sum:

#   abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)


