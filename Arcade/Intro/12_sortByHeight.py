import numpy as np

def sortByHeight(a):
    a=np.array(a)
    nottree=np.where(a!=-1)[0]
    people=a[nottree]
    people.sort()
    a[nottree]=people
    return(a)


def sortByHeight2(a):

    l = sorted([i for i in a if i > 0])
    for n,i in enumerate(a):
        if i == -1:
            l.insert(n,i)
    return l


a= [23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]

print(sortByHeight(a))
print(sortByHeight2(a))