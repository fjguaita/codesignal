def arithmeticExpression(a, b, c):  
    op=['+','-','*','/']
    
    return any([eval(f'{a}{i}{b}=={c}') for i in op])


a=1
b=2
c=4
op=['+','-','*','/']
print(([eval(f'{a}{i}{b}=={c}') for i in op]))


res=[1,2,3,4,5,6,7,8,9]
_, _, *res, _, _ = res


 # agrego un comentario por el tema de la rama

