# Two arrays are called similar if one can be obtained from another 
# by swapping at most one pair of elements in one of the arrays.

def areSimilar(A, B):
    return sorted(A)==sorted(B) and sum([a!=b for a,b in zip(A,B)])<=2


# sorted porque tienen que tener los mismos numeros
# entonces si hay alguno distinto ahi salta

# el otro condicional se fija si hay mas de 2 numeros en posiciones distintas


a= [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b= [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]

a2= [1, 1, 4]
b2= [1, 2, 3]

a3= [1, 2, 3]
b3= [2, 1, 3]


print(areSimilar(a, b))
print(areSimilar(a2, b2))
print(areSimilar(a3, b3))