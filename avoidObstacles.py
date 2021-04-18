# el inicio siempre es 0

import numpy as np
def avoidObstacles(a):

    a=np.array(sorted(a))
    for i in range(1,1002):
        b=np.arange(0,a[-1]+1,i)
        if all(n not in a for n in b):
            return i
    
# al ir desde 0 hasta 1000, el maximo salto que puede haber es 1001
# hay que contemplarlo xq los hdp lo pusieron en los hidden test


# este nunca se me hubiera ocurrido
# busca el resto de la division por x=2,3,4,5... de todos los elementos del array
# si el array que resulta no tienen ningun elemento nulo es xq no choca ninguno

def avoidObstacles2(a):
    c = 2
    while True:
        if sorted([i%c for i in a])[0]>0:
            return c
        c += 1



a1=[5, 3, 6, 7, 9]          #4
a2=[1, 4, 10, 6, 2]         #7
a3=[5, 8, 9, 13, 14]        #6
a4=[2,3]                    #4

import json
with open('test-12.json') as file:
    data = json.load(file)        

data=data['input']       # el resultado tiene q ser 1001
a5=data['inputArray']
print(avoidObstacles(a5))



