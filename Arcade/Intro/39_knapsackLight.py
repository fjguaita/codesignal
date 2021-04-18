# ¡Encontraste dos artículos en un cofre del tesoro! El primer artículo pesa peso1 y vale valor1, 
# y el segundo artículo pesa peso2 y vale valor2. ¿Cuál es el valor máximo total de los artículos 
# que puede llevar consigo, asumiendo que su capacidad máxima de peso es maxW y no puede volver por los artículos más tarde?

#T enga en cuenta que solo hay dos artículos y no puede traer más de un artículo de cada tipo, es decir, 
# no puede tomar dos primeros artículos o dos segundos artículos.



def knapsackLight(v1, w1, v2, w2, maxW):
    
    if maxW>=w1+w2:    
        return v1+v2
    if maxW<w1 and maxW<w2:
        return 0   
    if v1>=v2 and maxW>=w1:
        return v1
    return v2 if maxW>=w2 else v1


# la mas linda de siempre
def knapsackLight2(v1, w1, v2, w2, W):
    return max(int(w1<=W)*v1, int(w2<=W)*v2, int(w1+w2<=W)*(v1+v2))


v1= 15
w1= 2
v2= 20
w2= 3
maxW= 2

print(knapsackLight(v1, w1, v2, w2, maxW))
