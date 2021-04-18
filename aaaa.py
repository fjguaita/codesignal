from math import sqrt

def distEucl(p):
    return sqrt((p[1]-p[0])**2)

def closestPointPair(p):

    return min([distEucl(i) for i in p])



def closestPointPair2(p):
    return min([sqrt((i[1]-i[0])**2) for i in p])
    



p=([[0,1],[5,-3],[4,-5],[8,-3],[8,-3]])



print(closestPointPair(p))
print(closestPointPair2(p))


# habria que probar si no se pasa de tiempo