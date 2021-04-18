# Cada día, su altura aumenta en una cantidad fija representada por el número entero upSpeed. 
# Pero debido a la falta de luz solar, la planta disminuye en altura cada noche, en una cantidad representada por downSpeed.

#Dado que cultivó la planta a partir de una semilla, inicialmente comenzó a la altura 0. 
# Dado un número entero deseado de altura, su tarea es encontrar cuántos días le tomará a la planta alcanzar esta altura.

def growingPlant(upSpeed, downSpeed, desiredHeight):

    i=1
    Height=upSpeed
    while Height<desiredHeight:
        Height+=upSpeed-downSpeed
        i+=1
    return i


import math
def growingPlant(upSpeed, downSpeed, desiredHeight):
    
    return 1 if desiredHeight <= upSpeed else math.ceil((desiredHeight - upSpeed) / (upSpeed - downSpeed) + 1)



