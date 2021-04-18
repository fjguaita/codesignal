import numpy as np

def longestUncorruptedSegment(Sa, Da):
    
    Sa=np.array(Sa)
    Da=np.array(Da)
    pos=(np.where(Sa==Da)[0])


    flag=True
    suma=[0]
    seq=0
    indice=-1
    pos=[0]
    for a,b in zip(Sa,Da):
        indice+=1
        if a==b:
            suma[seq]+=1
            if flag:
                pos[seq]=indice 
                flag=False
        else:
            seq+=1
            suma.append(0)
            pos.append(0)
            flag =True
    i=suma.index(max(suma))  
    return [suma[i],pos[i]]


        

Sa= [33531593, 96933415, 28506400, 39457872, 29684716, 86010806]
Da= [33531593, 96913415, 28506400, 39457872, 29684716, 86010806]

print(longestUncorruptedSegment(Sa,Da))


# it works!!
