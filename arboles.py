import numpy as np
def sortByHeight(a):
    a=np.array(a)
    nottree=np.where(a!=-1)[0]
    people=a[nottree]
    people.sort()
    a[nottree]=people
    return(a)






a= [-1, 150, 190, 170, -1, -1, 160, 180]
print(sortByHeight(a))