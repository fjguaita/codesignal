import numpy as np
def matrixElementsSum(m):
    
    m=np.array(m)
    s=0
    while m.size>0:
        m=np.delete(m,np.where(m[0,:]==0),1)
        s+=sum(a for a in m[0,:])
        m=np.delete(m,0,0)
    return s
    

# este código cuenta por columna, desde abajo hasta arriba
# mientras no encuentre un cero sigue sumando

def matrixElementsSum2(m):
    s=0
    unzip = zip(*m)
    for i in unzip:
        for j in i:
            if(j==0):
                break
            else:
                s+=j
    return s


m=[[0,1,1,2], 
  [0,5,0,0], 
  [2,0,3,3]]

print(matrixElementsSum(m))


