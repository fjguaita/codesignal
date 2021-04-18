
def almostIncreasingSequence(s):
    f1 = sum([1 for a, b in zip(s[:-1], s[1:]) if a>=b ]) <= 1 
    f2 = sum([1 for a, c in zip(s[:-2], s[2:]) if a>=c ]) <= 1
    return f1 and f2



s1= [1, 3, 2, 4]


# s[:-1]    ->      [1,3,2]
# s[1:]     ->      [3,2,4]

# s[:-2]    ->      [2,4]
# s[2:]     ->      [1,3]

# la funcion zip arma la tupla    ->    (1,3)  (3,2)  (2,4)
# y se fija si el primero es mayor o igual al segundo   ->  suma 1 cada vez que esto pasa
# si la suma es mayor a 1 la función termina siendo falsa

# la segunda funcion hace lo mismo pero corre 2 posiciones la secuencia
# de esa forma soluciono el problema de que haya 2 numeros iguales seguidos




s2= [3, 6, 5, 8, 10, 20, 15]
s3= [10, 1, 2, 3, 4, 5]
s4= [1, 2, 1, 2]

print(almostIncreasingSequence(s1))
print(almostIncreasingSequence(s2))
print(almostIncreasingSequence(s3))
print(almostIncreasingSequence(s4))


# para entenderlo mejor veamos  s = [0 1 2 3 4 5 6 7 8 9]

# s[:-1]    ->      [0 1 2 3 4 5 6 7 8]
# s[1:]     ->      [1 2 3 4 5 6 7 8 9]

# s[:-2]    ->      [0 1 2 3 4 5 6 7]
# s[2:]     ->      [2 3 4 5 6 7 8 9]

# el de abajo siempre va a ser mayor
