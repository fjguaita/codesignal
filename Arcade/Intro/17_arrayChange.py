def arrayChange(a):

    target  = a[0] - 1
    steps = 0
    
    for i in a:
        if i > target: 
            target = i
        else:
            target = target + 1
            steps += target - i
            
    return steps



a1= [1, 1, 1]               # 3 mov
a2= [-1000, 0, -2, 0]       # 5 mov


print(arrayChange(a1))
print(arrayChange(a2))


# la secuencia debe ser creciente, no continua      ->      -1000 0 1 2     es creciente