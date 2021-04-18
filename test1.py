import numpy as np

def firstDuplicate(a):
    
    out=-1
    distancia=len(a)
    
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]==a[j]: 
                if j <= distancia:
                    out=a[i]
                    distancia=j
                break   
                
    return(out)

# el que hice yo no cumplia los últimos test por limite de tiempo



def firstDuplicate2(a):
    mySet=set()
    for i in a:
        if i in mySet:
            return i
        mySet.add(i)
    return -1


# este no entiendo como funciona
def firstDuplicate2(a):
    for i in a:
        a[abs(i)-1] *= -1
        print(f'{i}   {a}')
        if a[abs(i)-1] > 0:
            return abs(i)
    return -1


a=([28, 19, 13, 6, 34, 48, 50, 3, 47, 18, 15, 34, 16, 11, 13, 3, 2,
 4, 46, 6, 7, 3, 18, 9, 32, 21, 3, 21, 50, 10, 45, 13, 22, 1, 27, 18, 3, 27, 30, 44, 12, 30, 40, 1, 1, 31, 6, 18, 33, 5])

print(firstDuplicate2(a))









