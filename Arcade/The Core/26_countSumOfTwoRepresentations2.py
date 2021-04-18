def countSumOfTwoRepresentations2(n, l, r):
    b=0
    for i in range(l,r+1):
        b += sum([1 for j in range(i,r+1) if i+j==n ])
    return b

#el mio se pasa de tiempo

def countSumOfTwoRepresentations2(n, l, r):
    return sum(1 for a in range(l, r+1) if l <= a <= n - a <= r)



def countSumOfTwoRepresentations2(n, l, r):
    if l+r < n:
        l = n-r 
    else:
        r = n -l 
    if l > r:
        return 0
    return (r-l)//2 + 1


n1= 6
l1= 2
r1= 4
# salida = 2

n2= 6
l2= 3
r2= 3
# salida = 1

n3= 93
l3= 24
r3= 58
# salida = 12


print(countSumOfTwoRepresentations2(n1, l1, r1))
print(countSumOfTwoRepresentations2(n2, l2, r2))
print(countSumOfTwoRepresentations2(n3, l3, r3))


