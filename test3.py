# te dan una matriz y tenes que rotarla 90 grados (sentido agujas reloj)

import numpy as np
def rotateImage(a):
    
    return(np.rot90(a, -1))



def rotateImage2(a):
    a.reverse()
    for i in range(len(a)):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a



def rotateImage3(a):
    return list(zip(*reversed(a)))



def rotateImage4(a):
    return [[x[i] for x in a][::-1] for i in range(len(a))]




a=[[1,2,3], [4,5,6], [7,8,9]]

print(a)
print(rotateImage(a))