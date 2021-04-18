# dado un array, tengo que decir cuantos numeros faltan para que sea consecutivo creciente
# desde el menor hasta el mayor

def makeArrayConsecutive2(statues):
    
    return sum([1 for i in range(min(statues),max(statues)) if not i in statues])
        

# recorre el rango del menor al mayor numero que contiene el array
# por ej desde 2 hasta 8
# suma 1 cada vez que el numero no esta en el array



def makeArrayConsecutive22(statues):
    return max(statues) - min(statues) - len(statues) + 1


statues= [6, 2, 3, 8]


print(makeArrayConsecutive2(statues))

