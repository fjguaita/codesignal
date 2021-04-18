def arrayReplace(a, i, s):
       
    for j in range(len(a)):
        if a[j]==i:
            a[j]=s
    
    return a



# el mas elegante
def arrayReplace2(i, e, s):
    return [x if x!=e else s for x in i]





i=1
a=[1,2,1]
s=3

print(arrayReplace(a, i, s))
print(arrayReplace2(a, i, s))



